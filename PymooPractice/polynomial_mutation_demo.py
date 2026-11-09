"""NSGA-II lesson: bounded polynomial mutation on four example offspring."""
import random

rng = random.Random(1)


def polynomial_mutation(x, eta_m=20, mutation_prob=None, lower=0.0, upper=1.0):
    """Bounded polynomial mutation for real-valued decision variables."""
    if not x:
        raise ValueError("x must not be empty")
    if not lower < upper:
        raise ValueError("lower must be smaller than upper")
    if eta_m <= 0:
        raise ValueError("eta_m must be positive")

    n_var = len(x)
    if mutation_prob is None:
        mutation_prob = 1.0 / n_var
    if not 0 <= mutation_prob <= 1:
        raise ValueError("mutation_prob must be in [0, 1]")

    child = x.copy()  # do not change original list

    for i in range(n_var):
        if rng.random() >= mutation_prob:
            print(f"  变量{i+1}：未触发变异，保持 {child[i]:.3f}")
            continue

        y = child[i]
        if not lower <= y <= upper:
            raise ValueError("decision variable outside bounds")
        delta1 = (y - lower) / (upper - lower)
        delta2 = (upper - y) / (upper - lower)
        r = rng.random()
        power = 1.0 / (eta_m + 1.0)

        if r <= 0.5:
            val = 2.0 * r + (1.0 - 2.0 * r) * (1.0 - delta1) ** (eta_m + 1.0)
            delta_q = val ** power - 1.0
        else:
            val = 2.0 * (1.0 - r) + 2.0 * (r - 0.5) * (1.0 - delta2) ** (eta_m + 1.0)
            delta_q = 1.0 - val ** power

        new_y = y + delta_q * (upper - lower)
        child[i] = max(lower, min(upper, new_y))
        print(f"  变量{i+1}：触发变异，r={r:.3f}，{y:.3f} -> {child[i]:.3f}")

    return child


if __name__ == "__main__":
    crossover_offspring = [
        [0.2, 0.8],
        [0.2, 0.8],
        [0.78, 0.32],
        [0.22, 0.68],
    ]
    print("===== 多项式变异实验 =====")
    for k, x in enumerate(crossover_offspring, start=1):
        print(f"子代{k} 变异前：{x}")
        mutated = polynomial_mutation(x, eta_m=20, mutation_prob=0.5)
        print(f"子代{k} 变异后：{[round(v, 3) for v in mutated]}\n")
        assert len(mutated) == len(x)
        assert all(0.0 <= v <= 1.0 for v in mutated)
    print("[PASS] 子代维度和变量边界检查通过")

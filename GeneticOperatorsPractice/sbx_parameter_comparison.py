import numpy as np
from sbx_crossover import sbx_crossover

parent1 = np.array([0.2, 0.4, 0.6, 0.8])
parent2 = np.array([0.8, 0.6, 0.4, 0.2])

print("===== SBX 参数对比实验 =====")

for eta in [2, 5, 10, 20, 50]:

    rng = np.random.default_rng(42)

    child1, child2 = sbx_crossover(
        parent1,
        parent2,
        eta=eta,
        rng=rng
    )

    deviation = np.mean(
        np.abs(child1 - parent1)
    )

    print(
        f"eta={eta:2d} | "
        f"平均变化量={deviation:.6f}"
    )
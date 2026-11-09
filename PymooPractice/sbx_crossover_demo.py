
import random

# 两个独立的随机数生成器
rng_select = random.Random(42)
rng_sbx = random.Random(123)

# 种群：增加决策变量 x
population = [
    {"name": "A", "x": [0.2, 0.8], "rank": 1, "cd": float("inf")},
    {"name": "H", "x": [0.8, 0.2], "rank": 1, "cd": float("inf")},
    {"name": "E", "x": [0.6, 0.4], "rank": 1, "cd": 1.045},
    {"name": "B", "x": [0.3, 0.7], "rank": 1, "cd": 0.955}
]


# 1. 比较两个个体
def compare(a, b):
    if a["rank"] < b["rank"]:
        return a

    if b["rank"] < a["rank"]:
        return b

    if a["cd"] > b["cd"]:
        return a

    if b["cd"] > a["cd"]:
        return b

    return rng_select.choice([a, b])


# 2. 二元锦标赛选择
def tournament_selection(population):
    a, b = rng_select.sample(population, 2)
    winner = compare(a, b)

    print(f"{a['name']} vs {b['name']} -> {winner['name']}")

    return winner


# 3. SBX 模拟二进制交叉
def sbx_crossover(x1, x2, eta_c=2):
    child1 = []
    child2 = []

    # 对每一个决策变量进行交叉
    for i in range(len(x1)):
        a = x1[i]
        b = x2[i]

        # 产生随机数
        u = rng_sbx.random()

        # 计算 beta
        if u <= 0.5:
            beta = (2 * u) ** (1 / (eta_c + 1))
        else:
            beta = (1 / (2 * (1 - u))) ** (1 / (eta_c + 1))

        # 根据 beta 计算两个子代
        v1 = 0.5 * ((1 + beta) * a + (1 - beta) * b)
        v2 = 0.5 * ((1 - beta) * a + (1 + beta) * b)

        # 教学版：将变量限制在 [0, 1]
        v1 = max(0.0, min(1.0, v1))
        v2 = max(0.0, min(1.0, v2))

        # 保存新变量
        child1.append(v1)
        child2.append(v2)

        print(
            f"  变量 {i + 1}: "
            f"u={u:.3f}, beta={beta:.3f}, "
            f"子代=({v1:.3f}, {v2:.3f})"
        )

    return child1, child2


# 4. 使用锦标赛选择父代
mating_pool = []

print("===== 锦标赛选择 =====")

for _ in range(4):
    parent = tournament_selection(population)
    mating_pool.append(parent)


# 5. 两两配对，进行 SBX 交叉
offspring = []

print("\n===== SBX 交叉 =====")

for i in range(0, len(mating_pool), 2):
    p1 = mating_pool[i]
    p2 = mating_pool[i + 1]

    print(
        f"父代: {p1['name']} {p1['x']} "
        f"+ {p2['name']} {p2['x']}"
    )

    c1, c2 = sbx_crossover(
        p1["x"], p2["x"], eta_c=2
    )

    offspring.extend([c1, c2])


# 6. 输出所有子代
print("\n===== 子代决策变量 =====")

for i, x in enumerate(offspring, start=1):
    print(f"子代{i}: {[round(v, 3) for v in x]}")

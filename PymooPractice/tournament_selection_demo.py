
import random

# 固定随机种子，方便复现实验
rng = random.Random(42)

# 上一轮环境选择得到的四个解
population = [
    {"name": "A", "rank": 1, "cd": float("inf")},
    {"name": "H", "rank": 1, "cd": float("inf")},
    {"name": "E", "rank": 1, "cd": 1.045},
    {"name": "B", "rank": 1, "cd": 0.955}
]


# 比较两个候选解，返回胜出者
def compare(a, b):

    # 第一规则：Rank 越小越好
    if a["rank"] < b["rank"]:
        return a

    if b["rank"] < a["rank"]:
        return b

    # 第二规则：拥挤距离越大越好
    if a["cd"] > b["cd"]:
        return a

    if b["cd"] > a["cd"]:
        return b

    # 两项指标都相同，随机选择
    return rng.choice([a, b])


# 二元锦标赛
def tournament_selection(population):

    # 随机挑选两个不同的候选解
    a, b = rng.sample(population, 2)

    # 比赛，选出胜利者
    winner = compare(a, b)

    print(
        f"{a['name']} vs {b['name']}"
        f" -> 胜出：{winner['name']}"
    )

    return winner


# 连续进行四次锦标赛
mating_pool = []

for i in range(4):
    parent = tournament_selection(population)
    mating_pool.append(parent)

print("\n===== 选出的父代 =====")

for parent in mating_pool:
    print(parent["name"])

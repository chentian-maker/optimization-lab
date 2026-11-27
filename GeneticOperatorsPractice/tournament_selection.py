import numpy as np

# 创建随机数生成器
rng = np.random.default_rng(42)

# 个体名称
names = np.array(["A", "B", "C", "D", "E", "F"])

# 非支配等级
ranks = np.array([1, 1, 2, 2, 1, 3])

# 拥挤距离
crowding = np.array([0.8, 1.2, 2.5, 0.6, 0.3, 3.0])


def tournament(i, j, ranks, crowding, rng):

    # 第一优先级：比较非支配等级
    if ranks[i] < ranks[j]:
        return i

    if ranks[i] > ranks[j]:
        return j

    # 第二优先级：比较拥挤距离
    if crowding[i] > crowding[j]:
        return i

    if crowding[i] < crowding[j]:
        return j

    # 两项指标完全相同，随机选择
    return rng.choice([i, j])


print("===== 固定个体比赛 =====")

pairs = [(0, 2), (0, 1), (2, 3), (4, 5)]

for i, j in pairs:

    winner = tournament(i, j, ranks, crowding, rng)

    print(
        f"{names[i]} vs {names[j]} "
        f"-> {names[winner]}"
    )


print("\n===== 随机锦标赛 =====")

selected = []

for _ in range(10):

    # 随机抽取两个不同的个体
    i, j = rng.choice(
        len(names),
        size=2,
        replace=False
    )

    winner = tournament(i, j, ranks, crowding, rng)

    selected.append(winner)

    print(
        f"{names[i]} vs {names[j]} "
        f"-> {names[winner]}"
    )

print("\n最终选中的父代：", names[selected])
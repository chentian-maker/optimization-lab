
# 下一代环境选择（精英保留）
def select_next_population(fronts, crowding, population_size):

    # 用于保存选中的解
    selected = []

    # 按 Rank 从小到大处理各层
    for front in fronts:

        # 下一代还剩多少个位置
        remaining = population_size - len(selected)

        if remaining == 0:
            break

        # 情况1：当前层全部放得下
        if len(front) <= remaining:
            selected.extend(front)

        # 情况2：当前层放不下
        else:
            # 按拥挤距离从大到小排序
            ranked = sorted(
                front,
                key=lambda idx: crowding[idx],
                reverse=True
            )

            # 只选剩余名额对应的解
            selected.extend(ranked[:remaining])

            # 种群已满，结束选择
            break

    return selected


# 8 个候选解
names = ["A", "B", "D", "F", "C", "E", "G", "H"]

parents = [(1, 12), (3, 8), (5, 10), (8, 7)]
offspring = [(5, 7), (6, 4), (10, 5), (9, 1)]

# 父代与子代合并
points = parents + offspring

# 根据前面的手算结果预先给定各层
fronts = [
    [0, 1, 4, 5, 7],  # A B C E H
    [2, 3, 6]         # D F G
]

# 手算的第一层拥挤距离（近似值）
crowding = {
    0: float("inf"),  # A
    1: 0.955,         # B
    4: 0.739,         # C
    5: 1.045,         # E
    7: float("inf")   # H
}

# 下一代只能保留 4 个解
population_size = 4

selected = select_next_population(
    fronts,
    crowding,
    population_size
)

print("===== 下一代选择结果 =====")
for idx in selected:
    print(names[idx], points[idx])

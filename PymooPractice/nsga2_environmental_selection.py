
# ==========================================
# NSGA-II 环境选择：三个算法模块整合
# 所有目标均为最小化
# ==========================================

# 模块1-1：判断 a 是否支配 b
def dominates(a, b):
    better = False

    for i in range(len(a)):
        if a[i] > b[i]:
            return False
        if a[i] < b[i]:
            better = True

    return better


# 模块1-2：快速非支配排序
def fast_non_dominated_sort(points):
    size = len(points)

    # 每个解支配了哪些解
    dominated_sets = [[] for _ in range(size)]

    # 每个解被多少个解支配
    dominated_count = [0] * size

    # 保存每一层
    fronts = [[]]

    # 两两比较所有解
    for p in range(size):
        for q in range(size):
            if p == q:
                continue

            if dominates(points[p], points[q]):
                dominated_sets[p].append(q)

            elif dominates(points[q], points[p]):
                dominated_count[p] += 1

        if dominated_count[p] == 0:
            fronts[0].append(p)

    # 逐层寻找剩余的非支配解
    level = 0

    while True:
        next_front = []

        for p in fronts[level]:
            for q in dominated_sets[p]:
                dominated_count[q] -= 1

                if dominated_count[q] == 0:
                    next_front.append(q)

        if not next_front:
            break

        fronts.append(next_front)
        level += 1

    return fronts


# 模块2：计算拥挤距离
def crowding_distance(front, points):
    distances = {idx: 0.0 for idx in front}

    if len(front) <= 2:
        for idx in front:
            distances[idx] = float("inf")
        return distances

    # 按每一个目标分别计算
    for m in range(len(points[0])):

        order = sorted(
            front,
            key=lambda idx: points[idx][m]
        )

        lowest = points[order[0]][m]
        highest = points[order[-1]][m]

        if highest == lowest:
            continue

        # 边界解的拥挤距离设为无穷大
        distances[order[0]] = float("inf")
        distances[order[-1]] = float("inf")

        # 计算内部解
        for j in range(1, len(order) - 1):
            previous = points[order[j - 1]][m]
            following = points[order[j + 1]][m]

            contribution = (
                (following - previous)
                / (highest - lowest)
            )

            distances[order[j]] += contribution

    return distances


# 模块3：精英保留，选择下一代
def select_next_population(fronts, crowding, population_size):
    selected = []

    for front in fronts:
        remaining = population_size - len(selected)

        if remaining == 0:
            break

        # 当前层可以全部保留
        if len(front) <= remaining:
            selected.extend(front)

        # 当前层放不下：按照拥挤距离筛选
        else:
            ranked = sorted(
                front,
                key=lambda idx: crowding[idx],
                reverse=True
            )

            selected.extend(ranked[:remaining])
            break

    return selected


# ==========================================
# 主程序：准备父代和子代
# ==========================================

names = ["A", "B", "D", "F", "C", "E", "G", "H"]

parents = [
    (1, 12),   # A
    (3, 8),    # B
    (5, 10),   # D
    (8, 7)     # F
]

offspring = [
    (5, 7),    # C
    (6, 4),    # E
    (10, 5),   # G
    (9, 1)     # H
]

# 第一步：合并父代和子代
points = parents + offspring

# 第二步：自动非支配排序
fronts = fast_non_dominated_sort(points)

# 第三步：自动计算所有层的拥挤距离
crowding = {}

for front in fronts:
    result = crowding_distance(front, points)
    crowding.update(result)

# 查看自动计算的结果
print("===== 自动非支配排序和拥挤距离 =====")

for rank, front in enumerate(fronts, start=1):
    print(f"F{rank}:", [names[idx] for idx in front])

    for idx in front:
        print(f"  {names[idx]}: CD = {crowding[idx]:.3f}")

# 第四步：精英保留，生成下一代
population_size = 3

selected = select_next_population(
    fronts,
    crowding,
    population_size
)

print("\n===== 下一代（3个解）=====")

for idx in selected:
    print(names[idx], points[idx])

# 第五步：自动检查
assert set(names[idx] for idx in selected) == {"A", "E", "H"}
assert len(selected) == population_size

print("\n[PASS] 环境选择结果符合预期")

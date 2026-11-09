
# 1. 判断两个解之间的支配关系
def dominates(a, b):
    better = False

    for i in range(len(a)):
        if a[i] > b[i]:
            return False
        if a[i] < b[i]:
            better = True

    return better


# 2. 快速非支配排序
def fast_non_dominated_sort(points):
    size = len(points)

    # S[p]：解 p 支配了哪些解
    dominated_sets = [[] for _ in range(size)]

    # n[p]：有多少个解支配 p
    dominated_count = [0] * size

    # 存储每一层的解
    fronts = [[]]

    # 第一步：两两比较
    for p in range(size):
        for q in range(size):
            if p == q:
                continue

            if dominates(points[p], points[q]):
                dominated_sets[p].append(q)

            elif dominates(points[q], points[p]):
                dominated_count[p] += 1

        # 没有被任何解支配，属于第一层
        if dominated_count[p] == 0:
            fronts[0].append(p)

    # 保存初始计数，方便观察
    initial_counts = dominated_count.copy()

    # 第二步：逐层寻找其他非支配前沿
    i = 0

    while fronts[i]:
        next_front = []

        for p in fronts[i]:
            for q in dominated_sets[p]:
                dominated_count[q] -= 1

                if dominated_count[q] == 0:
                    next_front.append(q)

        i += 1
        fronts.append(next_front)

    # 删除最后产生的空层
    fronts.pop()

    return fronts, initial_counts


# 3. 准备测试数据
names = ["A", "B", "C", "D", "E", "F", "G"]

points = [
    (1, 7),
    (2, 5),
    (3, 4),
    (4, 6),
    (5, 2),
    (6, 3),
    (4, 8)
]

# 4. 调用排序函数
fronts, counts = fast_non_dominated_sort(points)

print("===== 初始支配计数 =====")

for i in range(len(names)):
    print(names[i], ":", counts[i])

print("\n===== 非支配排序结果 =====")

for i in range(len(fronts)):
    front_names = []

    for index in fronts[i]:
        front_names.append(names[index])

    print(f"F{i + 1} = {front_names}")

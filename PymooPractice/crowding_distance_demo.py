
# 计算同一非支配层中各解的拥挤距离
def crowding_distance(front, points):

    # 给当前层每个解的距离初始化为 0
    distances = {idx: 0.0 for idx in front}

    # 如果只有 0、1 或 2 个解
    if len(front) <= 2:
        for idx in front:
            distances[idx] = float("inf")
        return distances

    # 目标数量
    num_objectives = len(points[0])

    # 对每一个目标分别计算距离
    for m in range(num_objectives):

        # 按第 m 个目标从小到大排序
        order = sorted(
            front,
            key=lambda idx: points[idx][m]
        )
        print(f"当前目标 m={m}, 排序结果 order={order}")

        # 当前目标的最大值与最小值
        min_value = points[order[0]][m]
        max_value = points[order[-1]][m]

        # 边界解设置为无穷大
        distances[order[0]] = float("inf")
        distances[order[-1]] = float("inf")

        # 避免除以零
        if max_value == min_value:
            continue

        # 计算内部解的拥挤距离
        for j in range(1, len(order) - 1):
            previous = points[order[j - 1]][m]
            following = points[order[j + 1]][m]

            contribution = (
                (following - previous)
                / (max_value - min_value)
            )

            distances[order[j]] += contribution
            print(
                      f"解索引 {order[j]}，"
                      f"贡献={contribution:.2f}，"
                      f"累计距离={distances[order[j]]:.2f}"
                      )

    return distances


# 测试数据
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

# 第一层的索引：A、B、C、E
front = [0, 1, 2, 4]

result = crowding_distance(front, points)

print("===== 第一层拥挤距离 =====")

for idx in front:
    print(f"{names[idx]} : {result[idx]:.2f}")

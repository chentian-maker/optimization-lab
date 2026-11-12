
def reconstruct_path(parent, start, goal):

    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent[current]

    # 确认最终确实回到了起点
    if not path or path[-1] != start:
        return []

    path.reverse()

    return path


# 测试数据
parent = {
    "A": None,
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "D"
}

start = "A"
goal = "F"

# 执行路径恢复
if result:
    print("最短路径：", result)
    print("路径长度：", len(result) - 1)
else:
    print("未找到路径：终点不可达")
    print("路径长度：不存在")

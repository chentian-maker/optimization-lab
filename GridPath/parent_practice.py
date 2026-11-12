
from collections import deque

# 定义图
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

start = "A"
end = "D"

# 初始化队列、访问集合和前驱字典
queue = deque([start])
visited = {start}
parent = {start: None}

# BFS 搜索
while queue:
    current = queue.popleft()

    print("正在访问：", current)

    if current == end:
        break

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

# 从终点向起点还原路径
path = []

if end in visited:
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

print("前驱字典：", parent)
print("最短路径：", path)
print("路径长度：", len(path) - 1)

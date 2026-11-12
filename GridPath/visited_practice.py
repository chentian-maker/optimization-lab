
from collections import deque

# 创建一个简单的图
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# 创建队列
queue = deque(["A"])

# 记录已经发现的节点
visited = {"A"}

while queue:
    current = queue.popleft()
    print("当前访问：", current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("搜索结束")
print("已访问节点：", visited)

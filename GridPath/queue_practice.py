
from collections import deque

# 创建队列
queue = deque()

# 三个节点依次进入队列
queue.append("A")
queue.append("B")
queue.append("C")

print("初始队列：", list(queue))

# 取出最先进入的节点
first = queue.popleft()

print("取出的节点：", first)
print("剩余队列：", list(queue))

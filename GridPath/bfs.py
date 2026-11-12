
from collections import deque

from grid_map import grid, get_neighbors, is_walkable


def reconstruct_path(parent, start, goal):

    if goal not in parent:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if path[0] != start:
        return None

    return path


def bfs(grid, start, goal):

    # 检查起点和终点是否合法
    if not is_walkable(grid, start):
        return None

    if not is_walkable(grid, goal):
        return None

    # 初始化队列
    queue = deque([start])

    # 记录前驱节点
    parent = {start: None}

    # 访问计数
    visited_count = 0

    # 搜索日志
    search_log = []

    # 是否找到终点
    found = False

    while queue:

        # 取出队首节点
        current = queue.popleft()

        # 访问数量加一
        visited_count += 1

        # 记录新发现的邻居
        new_neighbors = []

        # 处理起点就是终点的情况
        if current == goal:
            found = True

        else:
            for neighbor in get_neighbors(grid, current):

                if neighbor not in parent:

                    # 记录前驱节点
                    parent[neighbor] = current

                    # 加入队列
                    queue.append(neighbor)

                    # 记录新邻居
                    new_neighbors.append(neighbor)

                    # 发现终点，立即停止扩展
                    if neighbor == goal:
                        found = True
                        break

        # 保存搜索记录
        search_log.append({
            "step": visited_count,
            "current": current,
            "new_neighbors": new_neighbors,
            "queue": list(queue)
        })

        # 找到终点，结束搜索
        if found:
            break

    # 输出访问统计
    print(f"\n访问节点数量：{visited_count}")

    # 输出搜索过程
    print("\n===== BFS 搜索过程 =====")

    for record in search_log:

        print(f"\n第 {record['step']} 步")
        print(f"当前访问：{record['current']}")
        print(f"新增邻居：{record['new_neighbors']}")
        print(f"队列：{record['queue']}")

    # 返回结果
    if found:
        return reconstruct_path(parent, start, goal)

    return None


if __name__ == "__main__":

    start = (0, 0)
    goal = (3, 3)

    path = bfs(grid, start, goal)

    print("\n===== BFS 路径搜索 =====")

    if path is None:
        print("没有找到可行路径")

    else:
        print("起点：", start)
        print("终点：", goal)
        print("最短路径：", path)
        print("路径长度：", len(path) - 1)
        print("经过节点数：", len(path))

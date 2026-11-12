
from grid_map import grid, get_neighbors, is_walkable


def reconstruct_path(parent, start, goal):

    # 如果没有找到终点
    if goal not in parent:
        return None

    path = []
    current = goal

    # 从终点向起点回溯
    while current is not None:

        path.append(current)

        current = parent[current]

    # 反转路径
    path.reverse()

    return path


def dfs(grid, start, goal):

    # 检查起点和终点是否合法
    if not is_walkable(grid, start):
        return None

    if not is_walkable(grid, goal):
        return None

    # 创建栈，起点先入栈
    stack = [start]

    # 记录前驱节点，同时标记已发现节点
    parent = {start: None}

    # 访问节点数量
    visited_count = 0

    # 搜索日志
    search_log = []

    # 是否找到终点
    found = False

    # 只要栈不为空，就继续搜索
    while stack:

        # 取出栈顶节点
        current = stack.pop()

        # 访问数量加一
        visited_count += 1

        # 记录新发现的邻居
        new_neighbors = []

        # 如果还没有到达终点
        if current != goal:

            for neighbor in get_neighbors(grid, current):

                # 避免重复发现节点
                if neighbor not in parent:

                    # 记录前驱节点
                    parent[neighbor] = current

                    # 邻居入栈
                    stack.append(neighbor)

                    # 记录新邻居
                    new_neighbors.append(neighbor)

        # 记录搜索过程
        search_log.append({
            "step": visited_count,
            "current": current,
            "new_neighbors": new_neighbors,
            "stack": list(stack)
        })

        # 判断是否到达终点
        if current == goal:

            found = True
            break

    # 输出访问数量
    print(f"\n访问节点数量：{visited_count}")

    # 输出搜索日志
    print("\n===== DFS 搜索过程 =====")

    for record in search_log:

        print(f"\n第 {record['step']} 步")
        print(f"当前访问：{record['current']}")
        print(f"新增邻居：{record['new_neighbors']}")
        print(f"栈：{record['stack']}")

    # 返回搜索结果
    if found:
        return reconstruct_path(parent, start, goal)

    return None


if __name__ == "__main__":

    start = (0, 0)
    goal = (3, 3)

    path = dfs(grid, start, goal)

    print("\n===== DFS 路径搜索 =====")

    if path is None:

        print("没有找到可行路径")

    else:

        print("起点：", start)
        print("终点：", goal)
        print("搜索路径：", path)
        print("路径长度：", len(path) - 1)
        print("经过节点数：", len(path))

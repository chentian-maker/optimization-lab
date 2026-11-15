
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
    return path


def dfs_recursive(grid, start, goal, return_details=False, verbose=True):

    # 检查起点和终点
    if not is_walkable(grid, start):
        return None

    if not is_walkable(grid, goal):
        return None

    # 初始化访问集合
    visited = {start}

    # 记录前驱节点
    parent = {start: None}

    # 搜索日志
    search_log = []

    # 递归搜索函数
    def visit(current, depth):

        record = {
            "step": len(search_log) + 1,
            "current": current,
            "depth": depth,
            "new_neighbors": []
        }

        search_log.append(record)

        # 找到终点
        if current == goal:
            return True

        # 按照原迭代 DFS 的搜索顺序遍历
        for neighbor in reversed(get_neighbors(grid, current)):

            if neighbor not in visited:

                # 标记当前发现的邻居
                visited.add(neighbor)

                # 记录前驱节点
                parent[neighbor] = current

                # 记录新邻居
                record["new_neighbors"].append(neighbor)

                # 立即递归深入
                if visit(neighbor, depth + 1):
                    return True

        # 当前分支无法到达终点，回溯
        return False

    # 开始搜索
    found = visit(start, 0)

    # 根据 verbose 决定是否打印
    if verbose:

        print(f"\n访问节点数量：{len(search_log)}")

        print("\n===== 递归 DFS 搜索过程 =====")

        for record in search_log:

            print(f"\n第 {record['step']} 步")
            print(f"当前访问：{record['current']}")
            print(f"递归深度：{record['depth']}")
            print(f"新增邻居：{record['new_neighbors']}")

    # 获取最终路径
    if found:
        path = reconstruct_path(parent, start, goal)
    else:
        path = None

    # 返回完整实验数据
    if return_details:

        return {
            "path": path,

            "visited": [
                record["current"]
                for record in search_log
            ],

            "search_log": search_log
        }

    # 默认只返回路径
    return path


if __name__ == "__main__":

    start = (0, 0)
    goal = (3, 3)

    path = dfs_recursive(grid, start, goal)

    print("\n===== 递归 DFS 路径搜索 =====")

    if path is None:
        print("没有找到可行路径")

    else:
        print("起点：", start)
        print("终点：", goal)
        print("搜索路径：", path)
        print("路径长度：", len(path) - 1)
        print("经过节点数：", len(path))


from collections import deque
from time import perf_counter
import csv

from grid_map import grid, get_neighbors, is_walkable


# =====================================
# 1. 公共函数：路径回溯
# =====================================

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


# =====================================
# 2. 公共函数：统一实验结果
# =====================================

def build_result(parent, start, goal, search_order, expanded_count):

    path = reconstruct_path(parent, start, goal)

    return {
        "found": path is not None,
        "discovered_count": len(parent),
        "expanded_count": expanded_count,
        "processed_count": len(search_order),
        "path_length": len(path) - 1 if path is not None else None,
        "path": path,
        "search_order": search_order
    }


# =====================================
# 3. 算法一：BFS
# =====================================

def bfs_search(grid, start, goal):

    if not is_walkable(grid, start):
        return build_result({}, start, goal, [], 0)

    if not is_walkable(grid, goal):
        return build_result({}, start, goal, [], 0)

    queue = deque([start])

    parent = {start: None}

    search_order = []

    expanded_count = 0

    while queue:

        current = queue.popleft()

        search_order.append(current)

        # 到达终点
        if current == goal:
            break

        expanded_count += 1

        for neighbor in get_neighbors(grid, current):

            if neighbor not in parent:

                parent[neighbor] = current

                queue.append(neighbor)

    return build_result(
        parent, start, goal, search_order, expanded_count
    )


# =====================================
# 4. 算法二：迭代 DFS
# =====================================

def iterative_dfs_search(grid, start, goal):

    if not is_walkable(grid, start):
        return build_result({}, start, goal, [], 0)

    if not is_walkable(grid, goal):
        return build_result({}, start, goal, [], 0)

    stack = [start]

    parent = {start: None}

    search_order = []

    expanded_count = 0

    while stack:

        current = stack.pop()

        search_order.append(current)

        if current == goal:
            break

        expanded_count += 1

        for neighbor in get_neighbors(grid, current):

            if neighbor not in parent:

                parent[neighbor] = current

                stack.append(neighbor)

    return build_result(
        parent, start, goal, search_order, expanded_count
    )


# =====================================
# 5. 算法三：递归 DFS
# =====================================

def recursive_dfs_search(grid, start, goal):

    if not is_walkable(grid, start):
        return build_result({}, start, goal, [], 0)

    if not is_walkable(grid, goal):
        return build_result({}, start, goal, [], 0)

    visited = {start}

    parent = {start: None}

    search_order = []

    expanded_count = 0

    def visit(current):

        nonlocal expanded_count

        search_order.append(current)

        if current == goal:
            return True

        expanded_count += 1

        for neighbor in reversed(get_neighbors(grid, current)):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                if visit(neighbor):
                    return True

        return False

    visit(start)

    return build_result(
        parent, start, goal, search_order, expanded_count
    )


# =====================================
# 6. 公共函数：运行时间测试
# =====================================

def benchmark(search_function, repeats=1000):

    if repeats < 1:
        raise ValueError("重复测试次数必须大于 0")

    # 预热，不计入正式测试
    search_function(grid, start, goal)

    result = None

    begin = perf_counter()

    for _ in range(repeats):

        result = search_function(grid, start, goal)

    end = perf_counter()

    average_time = (end - begin) / repeats * 1000

    result["runtime_ms"] = average_time

    return result


# =====================================
# 7. 主程序
# =====================================

if __name__ == "__main__":

    start = (0, 0)

    goal = (3, 3)

    repeats = 1000

    # 算法名称、算法函数、是否理论保证最短路径
    algorithms = [
        ("BFS", bfs_search, True),
        ("迭代 DFS", iterative_dfs_search, False),
        ("递归 DFS", recursive_dfs_search, False)
    ]

    results = []

    print("===== 图搜索算法综合实验 =====")

    print(f"起点：{start}")
    print(f"终点：{goal}")
    print(f"重复测试次数：{repeats}")

    # ---------------------------------
    # 获取最短路径基准
    # ---------------------------------

    # 当前问题是无权图，使用 BFS 获取最短路径基准
    optimal_result = bfs_search(grid, start, goal)

    optimal_path_length = optimal_result["path_length"]

    print(f"\n理论最短路径长度：{optimal_path_length}")

    # ---------------------------------
    # 运行三种算法
    # ---------------------------------

    for name, function, guarantees_shortest in algorithms:

        result = benchmark(function, repeats)

        # 理论上是否保证最短路径
        result["guarantees_shortest"] = guarantees_shortest

        # 最短路径保证的适用条件
        if guarantees_shortest:
            result["guarantee_condition"] = "无权图，每条边代价相同"
        else:
            result["guarantee_condition"] = "不保证最短路径"

        # 当前实验是否恰好找到最短路径
        result["is_shortest_this_run"] = (
            result["found"]
            and optimal_path_length is not None
            and result["path_length"] == optimal_path_length
        )

        # 保存理论最短路径长度
        result["optimal_path_length"] = optimal_path_length

        results.append((name, result))

    # ---------------------------------
    # 输出基础统计结果
    # ---------------------------------

    print("\n===== 算法对比结果 =====")

    print(
        f"{'算法':<12}"
        f"{'发现节点':<12}"
        f"{'展开节点':<12}"
        f"{'处理节点':<12}"
        f"{'路径长度':<12}"
        f"{'平均时间(ms)':<16}"
    )

    for name, result in results:

        path_length = (
            result["path_length"]
            if result["path_length"] is not None
            else "无路径"
        )

        print(
            f"{name:<12}"
            f"{result['discovered_count']:<12}"
            f"{result['expanded_count']:<12}"
            f"{result['processed_count']:<12}"
            f"{str(path_length):<12}"
            f"{result['runtime_ms']:<16.6f}"
        )

    # ---------------------------------
    # 输出算法正确性和最优性评价
    # ---------------------------------

    print("\n===== 算法要求与最优性评价 =====")

    for name, result in results:

        print(f"\n算法：{name}")

        print("是否找到路径：", result["found"])

        print(
            "理论保证最短路径：",
            "是" if result["guarantees_shortest"] else "否"
        )

        print(
            "本次结果是否最短：",
            "是" if result["is_shortest_this_run"] else "否"
        )

        print("保证条件：", result["guarantee_condition"])

        print("本次路径长度：", result["path_length"])

        print("理论最短路径长度：", result["optimal_path_length"])

    # ---------------------------------
    # 输出搜索顺序和路径
    # ---------------------------------

    print("\n===== 搜索路径对比 =====")

    for name, result in results:

        print(f"\n{name}")

        print("搜索顺序：", result["search_order"])

        print("最终路径：", result["path"])

    # ---------------------------------
    # 保存 CSV
    # ---------------------------------

    fields = [
        "algorithm",
        "found",
        "discovered_count",
        "expanded_count",
        "processed_count",
        "path_length",
        "runtime_ms",
        "guarantees_shortest",
        "guarantee_condition",
        "is_shortest_this_run",
        "optimal_path_length",
        "path",
        "search_order"
    ]

    with open(
        "comparison_results.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        writer.writeheader()

        for name, result in results:

            writer.writerow({

                "algorithm": name,

                "found": result["found"],

                "discovered_count": result["discovered_count"],

                "expanded_count": result["expanded_count"],

                "processed_count": result["processed_count"],

                "path_length": result["path_length"],

                "runtime_ms": result["runtime_ms"],

                "guarantees_shortest": result["guarantees_shortest"],

                "guarantee_condition": result["guarantee_condition"],

                "is_shortest_this_run": result["is_shortest_this_run"],

                "optimal_path_length": result["optimal_path_length"],

                "path": str(result["path"]),

                "search_order": str(result["search_order"])
            })

    print("\n实验数据已保存：comparison_results.csv")

    print("\n===== 实验完成 =====")

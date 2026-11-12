
import csv

from compare_search import (
    bfs_search,
    iterative_dfs_search,
    recursive_dfs_search
)

from grid_map import is_walkable


# =====================================
# 1. 定义测试地图
# =====================================

test_cases = [

    {
        "name": "空旷地图",
        "grid": [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (3, 3)
    },

    {
        "name": "障碍地图",
        "grid": [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 0]
        ],
        "start": (0, 0),
        "goal": (3, 3)
    },

    {
        "name": "不连通地图",
        "grid": [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        "start": (0, 0),
        "goal": (2, 2)
    },

    {
        "name": "起点等于终点",
        "grid": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        "start": (1, 1),
        "goal": (1, 1)
    },

    {
        "name": "终点不可通行",
        "grid": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ],
        "start": (0, 0),
        "goal": (2, 2)
    },

    {
        "name": "起点不可通行",
        "grid": [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (2, 2)
    }
]


# =====================================
# 2. 检查路径是否合法
# =====================================

def validate_path(grid, path, start, goal):

    if path is None or len(path) == 0:
        return False

    if path[0] != start:
        return False

    if path[-1] != goal:
        return False

    # 检查是否存在重复节点
    if len(path) != len(set(path)):
        return False

    # 检查每个节点是否可以通行
    for node in path:

        if not is_walkable(grid, node):
            return False

    # 检查相邻节点是否相邻
    for i in range(len(path) - 1):

        current = path[i]
        next_node = path[i + 1]

        distance = (
            abs(current[0] - next_node[0])
            + abs(current[1] - next_node[1])
        )

        if distance != 1:
            return False

    return True


# =====================================
# 3. 定义算法
# =====================================

algorithms = [

    ("BFS", bfs_search),

    ("迭代 DFS", iterative_dfs_search),

    ("递归 DFS", recursive_dfs_search)

]


# =====================================
# 4. 执行测试
# =====================================

total_tests = 0
passed_tests = 0

csv_results = []

print("===== 多地图算法正确性测试 =====")


for case in test_cases:

    name = case["name"]
    current_grid = case["grid"]
    start = case["start"]
    goal = case["goal"]

    print(f"\n===== 测试场景：{name} =====")

    # BFS 作为无权图最短路径基准
    reference = bfs_search(
        current_grid,
        start,
        goal
    )

    expected_found = reference["found"]
    optimal_length = reference["path_length"]

    print("预期是否可达：", expected_found)
    print("BFS 最短路径基准：", optimal_length)

    for algorithm_name, algorithm in algorithms:

        total_tests += 1

        result = algorithm(
            current_grid,
            start,
            goal
        )

        # 判断可达性是否正确
        reachability_correct = (
            result["found"] == expected_found
        )

        # 不可达时，路径合法性不适用
        if expected_found:

            path_valid = (
                result["found"]
                and validate_path(
                    current_grid,
                    result["path"],
                    start,
                    goal
                )
            )

            # 判断是否达到最短路径
            is_shortest = (
                path_valid
                and result["path_length"] == optimal_length
            )

        else:

            path_valid = None
            is_shortest = None

        # 基本正确性不要求 DFS 必须找到最短路径
        test_passed = (
            reachability_correct
            and (
                path_valid
                if expected_found
                else True
            )
        )

        if test_passed:
            passed_tests += 1

        print(f"\n算法：{algorithm_name}")

        print("是否找到路径：", result["found"])

        print("可达性判断正确：", reachability_correct)

        print(
            "路径是否合法：",
            path_valid if path_valid is not None else "N/A"
        )

        print(
            "是否达到最短路径：",
            is_shortest if is_shortest is not None else "N/A"
        )

        print(
            "路径长度：",
            result["path_length"]
        )

        print(
            "测试结果：",
            "PASS" if test_passed else "FAIL"
        )

        # 保存实验记录
        csv_results.append({

            "test_case": name,

            "algorithm": algorithm_name,

            "expected_found": expected_found,

            "found": result["found"],

            "reachability_correct": reachability_correct,

            "path_valid": (
                path_valid
                if path_valid is not None
                else "N/A"
            ),

            "path_length": result["path_length"],

            "optimal_path_length": optimal_length,

            "is_shortest": (
                is_shortest
                if is_shortest is not None
                else "N/A"
            ),

            "test_result": (
                "PASS" if test_passed else "FAIL"
            ),

            "path": str(result["path"])
        })


# =====================================
# 5. 保存 CSV
# =====================================

fields = [

    "test_case",
    "algorithm",
    "expected_found",
    "found",
    "reachability_correct",
    "path_valid",
    "path_length",
    "optimal_path_length",
    "is_shortest",
    "test_result",
    "path"
]

with open(
    "multi_map_test_results.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fields
    )

    writer.writeheader()

    writer.writerows(csv_results)


# =====================================
# 6. 输出总结
# =====================================

print("\n===== 测试总结 =====")

print("总测试次数：", total_tests)

print("通过次数：", passed_tests)

print("失败次数：", total_tests - passed_tests)

print("实验数据已保存：multi_map_test_results.csv")

if total_tests == passed_tests:

    print("[PASS] 所有算法正确性测试通过")

else:

    print("[FAIL] 存在未通过的测试")


import sys
import unittest
from pathlib import Path

# 将 GridPath 目录加入模块搜索路径
GRID_PATH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GRID_PATH))

from grid_map import grid
from bfs import bfs
from dfs import dfs
from dfs_recursive import dfs_recursive


class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        self.start = (0, 0)
        self.goal = (3, 3)

    # 测试1：BFS 能否找到路径
    def test_bfs_finds_path(self):
        result = bfs(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertIsNotNone(result["path"])

    # 测试2：BFS 是否找到最短路径
    def test_bfs_shortest_path(self):
        result = bfs(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertEqual(len(result["path"]) - 1, 6)

    # 测试3：迭代 DFS 能否找到路径
    def test_dfs_finds_path(self):
        result = dfs(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertIsNotNone(result["path"])

    # 测试4：递归 DFS 能否找到路径
    def test_recursive_dfs_finds_path(self):
        result = dfs_recursive(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertIsNotNone(result["path"])

    # 测试5：检查 BFS 访问记录和日志数量
    def test_bfs_log_consistency(self):
        result = bfs(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertEqual(
            len(result["visited"]),
            len(result["search_log"])
        )

    # 测试6：检查迭代 DFS 访问记录
    def test_dfs_log_consistency(self):
        result = dfs(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertEqual(
            len(result["visited"]),
            len(result["search_log"])
        )

    # 测试7：检查递归 DFS 访问记录
    def test_recursive_dfs_log_consistency(self):
        result = dfs_recursive(
            grid, self.start, self.goal,
            return_details=True,
            verbose=False
        )

        self.assertEqual(
            len(result["visited"]),
            len(result["search_log"])
        )

    # 测试8：起点是障碍物
    def test_blocked_start(self):
        test_grid = [
            [1, 0],
            [0, 0]
        ]

        result = bfs(
            test_grid, (0, 0), (1, 1),
            return_details=True,
            verbose=False
        )

        self.assertIsNone(result)

    # 测试9：终点是障碍物
    def test_blocked_goal(self):
        test_grid = [
            [0, 0],
            [0, 1]
        ]

        result = bfs(
            test_grid, (0, 0), (1, 1),
            return_details=True,
            verbose=False
        )

        self.assertIsNone(result)

    # 测试10：地图不连通
    def test_unreachable_goal(self):
        test_grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]

        result = bfs(
            test_grid, (0, 0), (0, 2),
            return_details=True,
            verbose=False
        )

        self.assertIsNone(result["path"])

        self.assertEqual(
            len(result["visited"]),
            len(result["search_log"])
        )


if __name__ == "__main__":
    unittest.main()

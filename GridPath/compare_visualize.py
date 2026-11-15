
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grid_map import grid
from bfs import bfs
from dfs import dfs
from dfs_recursive import dfs_recursive


def build_visual_grid(grid, visited, path, start, goal):

    # 复制原始地图
    visual_grid = [
        row.copy()
        for row in grid
    ]

    # 标记搜索区域
    for row, col in visited:

        if (row, col) != start and (row, col) != goal:
            visual_grid[row][col] = 2

    # 标记最终路径
    for row, col in path:

        if (row, col) != start and (row, col) != goal:
            visual_grid[row][col] = 3

    # 标记起点和终点
    visual_grid[start[0]][start[1]] = 4
    visual_grid[goal[0]][goal[1]] = 5

    return visual_grid


def draw_comparison(results, start, goal):

    colors = [
        "white",
        "gray",
        "lightblue",
        "red",
        "green",
        "yellow"
    ]

    cmap = ListedColormap(colors)

    # 创建一行三列的画布
    fig, axes = plt.subplots(
        1,
        3,
        figsize=(15, 5)
    )

    for ax, result in zip(axes, results):

        name = result["name"]
        data = result["data"]

        path = data["path"]
        visited = data["visited"]

        # 生成绘图数据
        visual_grid = build_visual_grid(
            grid,
            visited,
            path,
            start,
            goal
        )

        # 绘制地图
        ax.imshow(
            visual_grid,
            cmap=cmap,
            vmin=0,
            vmax=5
        )

        rows = len(grid)
        cols = len(grid[0])

        # 设置坐标轴
        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))

        ax.set_xticks(
            [x - 0.5 for x in range(cols + 1)],
            minor=True
        )

        ax.set_yticks(
            [y - 0.5 for y in range(rows + 1)],
            minor=True
        )

        ax.grid(
            which="minor",
            color="black",
            linewidth=1
        )

        ax.tick_params(
            which="minor",
            bottom=False,
            left=False
        )

        # 设置标题
        path_length = len(path) - 1

        ax.set_title(
            f"{name}\n"
            f"Path Length: {path_length}\n"
            f"Visited Nodes: {len(visited)}"
        )

        ax.set_xlabel("Column")
        ax.set_ylabel("Row")

    fig.suptitle(
        "Pathfinding Algorithm Comparison",
        fontsize=16
    )

    plt.tight_layout()

    # 保存图片
    save_path = "GridPath/algorithm_comparison_visualization.png"

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    print("对比图片已保存：", save_path)

    plt.show()


if __name__ == "__main__":

    start = (0, 0)
    goal = (3, 3)

    # 运行三种算法
    bfs_result = bfs(
        grid, start, goal,
        return_details=True,
        verbose=False
    )

    dfs_result = dfs(
        grid, start, goal,
        return_details=True,
        verbose=False
    )

    recursive_result = dfs_recursive(
        grid, start, goal,
        return_details=True,
        verbose=False
    )

    # 统一组织实验数据
    results = [
        {
            "name": "BFS",
            "data": bfs_result
        },
        {
            "name": "Iterative DFS",
            "data": dfs_result
        },
        {
            "name": "Recursive DFS",
            "data": recursive_result
        }
    ]

    # 输出实验结果
    print("===== 三种算法对比 =====")

    for result in results:

        name = result["name"]
        data = result["data"]

        path = data["path"]

        if path is None:
            print(name, "没有找到路径")
        else:
            print(
                f"{name}: "
                f"路径长度={len(path)-1}, "
                f"访问节点={len(data['visited'])}"
            )

    # 绘制对比图
    if all(item["data"]["path"] is not None for item in results):

        draw_comparison(
            results,
            start,
            goal
        )

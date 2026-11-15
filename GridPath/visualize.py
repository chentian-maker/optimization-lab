import os

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grid_map import grid
from bfs import bfs


def build_visual_grid(grid, visited, path, start, goal):
    # 复制地图，避免修改原始 grid
    visual_grid = [
        row.copy()
        for row in grid
    ]

    # 标记访问过的节点
    for row, col in visited:
        if (row, col) != start and (row, col) != goal:
            visual_grid[row][col] = 2

    # 标记最终路径
    for row, col in path:
        if (row, col) != start and (row, col) != goal:
            visual_grid[row][col] = 3

    # 标记起点和终点
    start_row, start_col = start
    goal_row, goal_col = goal
    visual_grid[start_row][start_col] = 4
    visual_grid[goal_row][goal_col] = 5

    return visual_grid


def draw_grid_image(visual_grid, title, save_path=None):
    rows = len(visual_grid)
    cols = len(visual_grid[0])

    colors = [
        "white",     # 0 未访问
        "gray",      # 1 障碍物
        "lightblue", # 2 已访问
        "red",       # 3 最终路径
        "green",     # 4 起点
        "yellow"     # 5 终点
    ]
    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.imshow(
        visual_grid,
        cmap=cmap,
        vmin=0,
        vmax=5
    )

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
        linewidth=1.5
    )

    ax.tick_params(
        which="minor",
        bottom=False,
        left=False
    )

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)
        print(f"图片已保存：{save_path}")

    plt.show()


def visualize_final_result(grid, visited, path, start, goal):
    visual_grid = build_visual_grid(
        grid, visited, path, start, goal
    )

    title = f"BFS Final Result\nPath Length: {len(path) - 1}"

    draw_grid_image(
        visual_grid,
        title,
        save_path="GridPath/bfs_visualization.png"
    )


def visualize_search_steps(grid, search_log, start, goal):
    output_dir = "GridPath/bfs_steps"
    os.makedirs(output_dir, exist_ok=True)

    visited_so_far = []

    for i, record in enumerate(search_log, start=1):
        visited_so_far.append(record["current"])

        visual_grid = build_visual_grid(
            grid=grid,
            visited=visited_so_far,
            path=[],
            start=start,
            goal=goal
        )

        title = f"BFS Step {i}\nCurrent: {record['current']}"

        save_path = os.path.join(
            output_dir,
            f"bfs_step_{i:02d}.png"
        )

        draw_grid_image(
            visual_grid,
            title,
            save_path=save_path
        )


if __name__ == "__main__":
    start = (0, 0)
    goal = (3, 3)

    result = bfs(
        grid,
        start,
        goal,
        return_details=True,
        verbose=False
    )

    path = result["path"]
    visited = result["visited"]
    search_log = result["search_log"]

    if path is None:
        print("没有找到可行路径")
    else:
        # 1. 画最终结果图
        visualize_final_result(
            grid,
            visited,
            path,
            start,
            goal
        )

        # 2. 画每一步搜索过程图
        visualize_search_steps(
            grid,
            search_log,
            start,
            goal
        )
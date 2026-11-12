
# 网格地图
# 0 表示可以通行
# 1 表示障碍物

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]


# 判断坐标是否在地图范围内
def in_bounds(grid, position):

    row, col = position

    return (
        0 <= row < len(grid)
        and 0 <= col < len(grid[0])
    )


# 判断当前位置是否可以通行
def is_walkable(grid, position):

    if not in_bounds(grid, position):
        return False

    row, col = position

    return grid[row][col] == 0


# 获取当前位置的合法邻居
def get_neighbors(grid, position):

    if not is_walkable(grid, position):
        return []

    row, col = position

    # 上、下、左、右
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:

        new_position = (
            row + dr,
            col + dc
        )

        if is_walkable(grid, new_position):
            neighbors.append(new_position)

    return neighbors


# 程序测试
if __name__ == "__main__":

    print("===== 网格地图 =====")

    for row in grid:
        print(row)

    print("\n===== 邻居测试 =====")

    test_positions = [
        (0, 0),
        (2, 1),
        (3, 3),
        (1, 1),
        (-1, 0)
    ]

    for position in test_positions:

        neighbors = get_neighbors(grid, position)

        print(position, "->", neighbors)

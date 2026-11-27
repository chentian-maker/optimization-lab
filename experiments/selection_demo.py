import numpy as np

from optimization_lab.algorithms.selection import (
    tournament_selection
)


rng = np.random.default_rng(42)

# 创建一个模拟种群
X = rng.random((100, 30))

# 模拟非支配等级
ranks = rng.integers(1, 4, size=100)

# 模拟拥挤距离
crowding = rng.random(100)

# 选择100个父代
selected = tournament_selection(
    ranks=ranks,
    crowding=crowding,
    n_select=100,
    rng=rng
)

# 根据下标提取决策变量
parents = X[selected]

print("===== 工程选择算子实验 =====")
print("原始种群形状：", X.shape)
print("父代下标形状：", selected.shape)
print("父代种群形状：", parents.shape)

print("前10个父代下标：", selected[:10])

print(
    "下标是否合法：",
    np.all((selected >= 0) & (selected < 100))
)

print(
    "原始种群平均Rank：",
    np.mean(ranks)
)

print(
    "选中父代平均Rank：",
    np.mean(ranks[selected])
)
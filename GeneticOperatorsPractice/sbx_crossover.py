import numpy as np


def sbx_crossover(parent1, parent2, eta=20, rng=None):

    if rng is None:
        rng = np.random.default_rng()

    # 转换为浮点数组
    parent1 = np.asarray(parent1, dtype=float)
    parent2 = np.asarray(parent2, dtype=float)

    # 获取决策变量数量
    n_var = len(parent1)

    # 为每个决策变量生成随机数
    u = rng.random(n_var)

    # 创建 beta 数组
    beta = np.zeros(n_var)

    # 当 u <= 0.5 时
    mask = u <= 0.5

    beta[mask] = (
        2 * u[mask]
    ) ** (1 / (eta + 1))

    # 当 u > 0.5 时
    beta[~mask] = (
        1 / (2 * (1 - u[~mask]))
    ) ** (1 / (eta + 1))

    # 计算父代中心位置
    center = (parent1 + parent2) / 2

    # 计算父代之间的半间距
    distance = (parent2 - parent1) / 2

    # 生成两个子代
    child1 = center - beta * distance
    child2 = center + beta * distance

    # 边界处理
    child1 = np.clip(child1, 0.0, 1.0)
    child2 = np.clip(child2, 0.0, 1.0)

    return child1, child2


# 固定随机种子
rng = np.random.default_rng(42)

parent1 = np.array([0.2, 0.4, 0.6, 0.8])
parent2 = np.array([0.8, 0.6, 0.4, 0.2])

child1, child2 = sbx_crossover(
    parent1,
    parent2,
    eta=20,
    rng=rng
)

print("===== SBX 交叉实验 =====")

print("父代1：", parent1)
print("父代2：", parent2)

print("子代1：", child1)
print("子代2：", child2)

print("子代1形状：", child1.shape)
print("子代2形状：", child2.shape)

print(
    "子代1是否满足边界：",
    np.all((child1 >= 0) & (child1 <= 1))
)

print(
    "子代2是否满足边界：",
    np.all((child2 >= 0) & (child2 <= 1))
)
import numpy as np

from optimization_lab.algorithms.crossover import (
    sbx_crossover
)


rng = np.random.default_rng(42)

parent1 = np.array([-3.0, 0.2, 6.0])
parent2 = np.array([3.0, 0.8, -6.0])

# 每个变量具有不同的取值范围
xl = np.array([-5.0, 0.0, -10.0])
xu = np.array([5.0, 1.0, 10.0])

child1, child2 = sbx_crossover(
    parent1,
    parent2,
    xl=xl,
    xu=xu,
    eta=20,
    prob=1.0,
    prob_var=1.0,
    rng=rng
)

print("===== 工程 SBX 交叉实验 =====")

print("变量下界：", xl)
print("变量上界：", xu)

print("父代1：", parent1)
print("父代2：", parent2)

print("子代1：", child1)
print("子代2：", child2)

print("子代1形状：", child1.shape)
print("子代2形状：", child2.shape)

print(
    "子代1边界检查：",
    np.all((child1 >= xl) & (child1 <= xu))
)

print(
    "子代2边界检查：",
    np.all((child2 >= xl) & (child2 <= xu))
)

print(
    "父代数据是否保持不变：",
    np.array_equal(parent1, [-3.0, 0.2, 6.0])
    and np.array_equal(parent2, [3.0, 0.8, -6.0])
)
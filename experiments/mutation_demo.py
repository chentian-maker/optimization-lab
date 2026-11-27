import numpy as np

from optimization_lab.algorithms.mutation import (
    polynomial_mutation
)


rng = np.random.default_rng(42)

parent = np.array([-3.0, 0.2, 6.0])

xl = np.array([-5.0, 0.0, -10.0])
xu = np.array([5.0, 1.0, 10.0])

# 保存原始数据
original = parent.copy()

child = polynomial_mutation(
    parent,
    xl=xl,
    xu=xu,
    eta=20,
    prob=1.0,
    rng=rng
)

print("===== 工程多项式变异实验 =====")

print("变量下界：", xl)
print("变量上界：", xu)

print("变异前：", parent)
print("变异后：", child)

print("变量变化量：", child - parent)
print("子代形状：", child.shape)

print(
    "边界检查：",
    np.all((child >= xl) & (child <= xu))
)

print(
    "父代数据是否保持不变：",
    np.array_equal(parent, original)
)

# 验证变异概率为0的情况
no_mutation = polynomial_mutation(
    parent,
    xl=xl,
    xu=xu,
    prob=0.0,
    rng=rng
)

print(
    "零变异概率检查：",
    np.array_equal(no_mutation, parent)
)
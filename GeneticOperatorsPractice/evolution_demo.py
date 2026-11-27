import numpy as np

# 固定随机种子，保证实验可以复现
rng = np.random.default_rng(42)

# 创建两个父代个体
parent1 = np.array([0.2, 0.4, 0.6, 0.8])
parent2 = np.array([0.9, 0.7, 0.5, 0.3])

# 简单的单点交叉
child = np.concatenate([
    parent1[:2],
    parent2[2:]
])

print("===== 遗传算子基础实验 =====")
print("父代1：", parent1)
print("父代2：", parent2)
print("交叉后的子代：", child)

# 保存变异前的个体
before_mutation = child.copy()

# 随机选择一个决策变量
index = rng.integers(0, len(child))

# 产生随机扰动
delta = rng.uniform(-0.2, 0.2)

# 执行变异
child[index] += delta

# 保证变量仍然处于合法范围
child = np.clip(child, 0.0, 1.0)

print("变异位置：", index)
print("变异幅度：", delta)
print("变异前：", before_mutation)
print("变异后：", child)
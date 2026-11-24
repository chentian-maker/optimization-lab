import numpy as np

# 创建决策变量矩阵
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("===== NumPy axis 实验 =====")

print("原始矩阵：")
print(X)

print("矩阵形状：", X.shape)

# 对每一列求和
print("axis=0：", np.sum(X, axis=0))

# 对每一行求和
print("axis=1：", np.sum(X, axis=1))

# 对所有元素求和
print("全部求和：", np.sum(X))

# 计算每个个体的变量平均值
print("个体平均值：", np.mean(X, axis=1))

# 计算每个决策变量的平均值
print("变量平均值：", np.mean(X, axis=0))
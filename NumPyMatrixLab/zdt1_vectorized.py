import numpy as np


def zdt1_batch(X):

    # 获取每个个体的决策变量数量
    n_var = X.shape[1]

    # 计算所有个体的第一目标函数
    f1 = X[:, 0]

    # 计算所有个体的辅助函数 g
    g = 1 + 9 * np.sum(X[:, 1:], axis=1) / (n_var - 1)

    # 计算所有个体的第二目标函数
    f2 = g * (1 - np.sqrt(f1 / g))

    # 将两个目标值合并成矩阵
    F = np.column_stack((f1, f2))

    return F


# 创建测试种群
X = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.2, 0.3, 0.4, 0.5],
    [0.3, 0.4, 0.5, 0.6]
])

# 批量计算目标函数
F = zdt1_batch(X)

print("===== ZDT1 批量计算实验 =====")

print("决策变量矩阵：")
print(X)

print("决策变量矩阵形状：", X.shape)

print("\n目标函数矩阵：")
print(F)

print("目标函数矩阵形状：", F.shape)

# 创建100个个体，每个个体30个变量
rng = np.random.default_rng(42)

X_large = rng.random((100, 30))

F_large = zdt1_batch(X_large)

print("\n===== 大规模种群实验 =====")
print("种群矩阵形状：", X_large.shape)
print("目标矩阵形状：", F_large.shape)

print("前5个个体的目标值：")
print(F_large[:5])
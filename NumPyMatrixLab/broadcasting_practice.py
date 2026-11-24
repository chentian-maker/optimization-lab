import numpy as np

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([10, 20, 30])

print("===== 广播机制实验 =====")

print("原始矩阵：")
print(X)

print("矩阵形状：", X.shape)
print("向量形状：", b.shape)

# 实验1：矩阵与标量相加
print("\n实验1：矩阵加10")
print(X + 10)

# 实验2：矩阵与向量相加
print("\n实验2：矩阵加向量")
print(X + b)

# 实验3：矩阵与向量逐元素相乘
print("\n实验3：矩阵乘向量")
print(X * b)

# 实验4：多目标优化边界修复
xl = np.array([2, 3, 4])
xu = np.array([6, 7, 8])

Y = np.clip(X, xl, xu)

print("\n实验4：边界修复")
print(Y)

print("修复后矩阵形状：", Y.shape)
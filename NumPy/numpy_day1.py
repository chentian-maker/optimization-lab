import numpy as np

# 创建矩阵
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 查看矩阵形状和数据类型
print("矩阵 A：")
print(A)
print("shape:", A.shape)
print("dtype:", A.dtype)

# 矩阵转置
print("转置矩阵：")
print(A.T)
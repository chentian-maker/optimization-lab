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

# =========================
# 实验二：矩阵乘法
# =========================

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("矩阵 B：")
print(B)

# 使用 @ 进行矩阵乘法
C = A @ B

print("矩阵乘法结果 C：")
print(C)

print("矩阵 A 的形状：", A.shape)
print("矩阵 B 的形状：", B.shape)
print("矩阵 C 的形状：", C.shape)

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
# 实验三：reshape 改变数组形状

D = np.arange(1, 13)

print("一维数组：")
print(D)

E = D.reshape(3, 4)

print("变成 3 行 4 列：")
print(E)

print("数组形状：", E.shape)
# 实验四：索引和切片

print("第一行：")
print(E[0, :])

print("第二行第三列：")
print(E[1, 2])

print("所有行的第二列：")
print(E[:, 1])

print("前两行、前两列：")
print(E[0:2, 0:2])
# 实验五：数据类型

print("整数数组的数据类型：", E.dtype)

F = np.array([1.5, 2.5, 3.5])

print("浮点数数组的数据类型：", F.dtype)
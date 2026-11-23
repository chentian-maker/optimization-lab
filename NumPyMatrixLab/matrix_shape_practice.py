
import numpy as np

# 假设有100个个体，每个个体30个变量
rng = np.random.default_rng(42)

X = rng.random((100, 30))

# 构造30×2的权重矩阵
W = rng.random((30, 2))

# 矩阵乘法
Y = X @ W

print("===== 多目标优化矩阵尺寸实验 =====")

print("决策变量矩阵 X：", X.shape)
print("权重矩阵 W：", W.shape)
print("变换结果矩阵 Y：", Y.shape)

print("\n第一个个体的前5个变量：")
print(X[0, :5])

print("\n第一个个体的变换结果：")
print(Y[0])

# 检查结果是否符合预期
assert Y.shape == (100, 2)

print("\n[PASS] 矩阵尺寸检查通过！")

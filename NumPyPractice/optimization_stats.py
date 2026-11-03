
import numpy as np

# 5 个候选解，每个解包含 2 个目标值
# 第一列是成本，第二列是能耗
objectives = np.array([
    [100, 50],
    [120, 40],
    [90, 65],
    [110, 45],
    [95, 55]
])

print("===== 多目标优化实验数据 =====")
print(objectives)

# 查看数组结构
print("\n===== 数组基本信息 =====")
print("shape:", objectives.shape)
print("dtype:", objectives.dtype)
print("ndim:", objectives.ndim)

# 按列统计
print("\n===== 各目标统计量 =====")
print("平均值:", np.mean(objectives, axis=0))
print("标准差:", np.std(objectives, axis=0))
print("最小值:", np.min(objectives, axis=0))
print("最大值:", np.max(objectives, axis=0))

# 按行统计
print("\n===== 每个方案的行平均值 =====")
print(np.mean(objectives, axis=1))

# 取出单独的目标数据
cost = objectives[:, 0]
energy = objectives[:, 1]

print("\n===== 单独提取目标 =====")
print("成本:", cost)
print("能耗:", energy)

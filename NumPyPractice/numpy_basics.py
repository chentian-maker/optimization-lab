
import numpy as np

# 1. 创建一维数组
arr = np.array([10, 20, 30, 40, 50])

print("===== 数组基本信息 =====")
print("数组：", arr)
print("shape：", arr.shape)
print("dtype：", arr.dtype)
print("ndim：", arr.ndim)

# 2. 索引与切片
print("\n===== 索引和切片 =====")
print("第一个元素：", arr[0])
print("最后一个元素：", arr[-1])
print("前3个元素：", arr[:3])
print("第2到第4个元素：", arr[1:4])

# 3. 统计量
print("\n===== 统计分析 =====")
print("平均值：", np.mean(arr))
print("标准差：", np.std(arr))
print("最小值：", np.min(arr))
print("最大值：", np.max(arr))

# 4. 二维数组
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n===== 二维数组 =====")
print(matrix)
print("shape：", matrix.shape)
print("dtype：", matrix.dtype)
print("第2行第3列：", matrix[1, 2])

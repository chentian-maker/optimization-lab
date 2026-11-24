import numpy as np
import time

# 创建包含100万个元素的数组
X = np.arange(1000000, dtype=np.float64)

print("===== 向量化计算性能实验 =====")
print("数据数量：", X.size)

# 方法1：传统Python循环
start = time.perf_counter()

Y1 = []

for x in X:
    Y1.append(x ** 2)

Y1 = np.array(Y1)

end = time.perf_counter()

loop_time = end - start

# 方法2：NumPy向量化计算
start = time.perf_counter()

Y2 = X ** 2

end = time.perf_counter()

numpy_time = end - start

# 验证计算结果是否一致
same = np.allclose(Y1, Y2)

print("\n===== 计算结果 =====")
print("循环计算前5个结果：", Y1[:5])
print("向量化前5个结果：", Y2[:5])
print("计算结果一致：", same)

print("\n===== 性能对比 =====")
print(f"循环计算时间：{loop_time:.6f} 秒")
print(f"向量化计算时间：{numpy_time:.6f} 秒")

print(f"加速倍数：{loop_time / numpy_time:.2f}")
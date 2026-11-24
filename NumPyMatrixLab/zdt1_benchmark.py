import numpy as np
import time


# 方法1：传统循环计算
def zdt1_loop(X):

    F = []

    for x in X:

        n_var = len(x)

        f1 = x[0]

        g = 1 + 9 * sum(x[1:]) / (n_var - 1)

        f2 = g * (1 - np.sqrt(f1 / g))

        F.append([f1, f2])

    return np.array(F)


# 方法2：NumPy向量化计算
def zdt1_batch(X):

    n_var = X.shape[1]

    f1 = X[:, 0]

    g = 1 + 9 * np.sum(
        X[:, 1:], axis=1
    ) / (n_var - 1)

    f2 = g * (1 - np.sqrt(f1 / g))

    return np.column_stack((f1, f2))


# 创建随机种群
rng = np.random.default_rng(42)

X = rng.random((10000, 30))

print("===== ZDT1 性能对比实验 =====")
print("种群形状：", X.shape)


# 重复测试并计算平均运行时间
def benchmark(func, X, repeats=10):

    times = []

    for _ in range(repeats):

        start = time.perf_counter()

        F = func(X)

        end = time.perf_counter()

        times.append(end - start)

    return F, np.mean(times)


# 测试两种方法
F1, loop_time = benchmark(zdt1_loop, X)

F2, batch_time = benchmark(zdt1_batch, X)


# 正确性验证
same = np.allclose(
    F1, F2, rtol=1e-10, atol=1e-12
)

max_error = np.max(np.abs(F1 - F2))


print("\n===== 正确性验证 =====")

print("循环计算结果形状：", F1.shape)
print("批量计算结果形状：", F2.shape)

print("计算结果一致：", same)

print(f"最大绝对误差：{max_error:.12e}")


print("\n===== 性能对比 =====")

print(f"循环平均时间：{loop_time:.6f} 秒")

print(f"批量平均时间：{batch_time:.6f} 秒")

print(f"加速倍数：{loop_time / batch_time:.2f}")


# 自动验收
assert F1.shape == (10000, 2)
assert F2.shape == (10000, 2)
assert same

print("\n[PASS] ZDT1 批量计算验证通过")
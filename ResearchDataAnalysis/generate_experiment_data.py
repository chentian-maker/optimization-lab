
from pathlib import Path

import numpy as np
import pandas as pd


# 1. 创建随机数生成器
# 固定种子，使多次运行可以复现相同数据
rng = np.random.default_rng(42)


# 2. 设置三个算法的模拟基础指标
# 顺序为：IGD、HV、运行时间（秒）
algorithms = {
    "NSGA-II": (0.085, 0.78, 2.0),
    "MOEA/D": (0.072, 0.82, 1.6),
    "NSGA-III": (0.060, 0.85, 2.4),
}


# 3. 设置不同测试函数带来的模拟偏移
problems = {
    "DTLZ1": (0.03, -0.05, 0.5),
    "DTLZ2": (0.00, 0.00, 0.0),
    "DTLZ3": (0.06, -0.10, 1.0),
}


# 4. 生成实验记录
records = []

for algorithm, base in algorithms.items():
    for problem, offset in problems.items():
        for run in range(1, 11):

            # 正态分布模拟不同实验的随机波动
            igd = rng.normal(base[0] + offset[0], 0.012)
            hv = rng.normal(base[1] + offset[1], 0.025)
            runtime = rng.normal(base[2] + offset[2], 0.2)

            # 限制数据在预设的有效范围
            igd = max(0.0, igd)
            hv = np.clip(hv, 0.0, 1.0)
            runtime = max(0.01, runtime)

            records.append({
                "algorithm": algorithm,
                "problem": problem,
                "run": run,
                "igd": round(float(igd), 4),
                "hv": round(float(hv), 4),
                "runtime_s": round(float(runtime), 4),
            })


# 5. 转换为 DataFrame
df = pd.DataFrame(records)


# 6. 故意制造有问题的数据
# 后面的数据清洗练习需要检测这些问题
df.loc[5, "igd"] = np.nan
df.loc[35, "hv"] = np.nan
df.loc[67, "runtime_s"] = -3.0


# 7. 创建输出文件夹
data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)


# 8. 保存为 CSV
output_path = data_dir / "multi_algorithm_results.csv"

df.to_csv(output_path, index=False, encoding="utf-8-sig")


# 9. 检查结果
print("===== 多算法科研实验数据 =====")
print("数据形状：", df.shape)

print("\n前5行：")
print(df.head())

print("\n缺失值统计：")
print(df.isna().sum())

print("\n负数运行时间数量：")
print((df["runtime_s"] < 0).sum())

print("\n文件已保存：", output_path)

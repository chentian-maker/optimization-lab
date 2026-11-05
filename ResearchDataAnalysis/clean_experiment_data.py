
from pathlib import Path
import pandas as pd


# ===== 1. 设置文件路径 =====

# 当前 Python 文件所在文件夹
base_dir = Path(__file__).resolve().parent

# 原始实验数据路径
input_path = base_dir / "data" / "multi_algorithm_results.csv"

# 清洗结果保存位置
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)


# ===== 2. 读取原始数据 =====

df = pd.read_csv(input_path)

print("===== 原始数据检查 =====")
print("原始数据总行数：", len(df))

print("\n各列缺失值数量：")
print(df.isna().sum())


# ===== 3. 检查异常数据 =====

# 检查 IGD、HV、运行时间是否有缺失
missing_mask = df[["igd", "hv", "runtime_s"]].isna().any(axis=1)

# IGD 是距离指标，不能为负数
invalid_igd = df["igd"] < 0

# 本次模拟数据中的 HV 已限制在 0 到 1
invalid_hv = ~df["hv"].between(0, 1)

# 运行时间必须大于 0
invalid_runtime = df["runtime_s"] <= 0

# 任意一项出现问题，标记为异常记录
invalid_mask = (
    missing_mask
    | invalid_igd
    | invalid_hv
    | invalid_runtime
)


# ===== 4. 分离有效和异常数据 =====

clean_df = df.loc[~invalid_mask].copy()
invalid_df = df.loc[invalid_mask].copy()

print("\n===== 清洗结果 =====")
print("有效数据：", len(clean_df))
print("异常数据：", len(invalid_df))

print("\n异常数据详情：")
print(invalid_df.to_string(index=False))


# ===== 5. 保存处理后的数据 =====

clean_path = output_dir / "clean_results.csv"
invalid_path = output_dir / "invalid_results.csv"

clean_df.to_csv(clean_path, index=False, encoding="utf-8-sig")
invalid_df.to_csv(invalid_path, index=False, encoding="utf-8-sig")

print("\n清洗数据已保存：", clean_path)
print("异常数据已保存：", invalid_path)


# ===== 6. 进行双重分组统计 =====

summary = clean_df.groupby(
    ["algorithm", "problem"]
).agg(
    runs=("run", "count"),
    igd_mean=("igd", "mean"),
    igd_std=("igd", "std"),
    hv_mean=("hv", "mean"),
    hv_std=("hv", "std"),
    runtime_mean=("runtime_s", "mean")
).round(4)

print("\n===== 算法性能统计 =====")
print(summary.to_string())

summary.to_csv(
    output_dir / "algorithm_summary.csv",
    encoding="utf-8-sig"
)

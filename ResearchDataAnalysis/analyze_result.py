
# 导入 Pandas 库
import pandas as pd
import matplotlib

# 使用无需弹出图形窗口的绘图后端
matplotlib.use("Agg")

import matplotlib.pyplot as plt
# 用于管理文件路径
from pathlib import Path

# 1. 找到当前 Python 文件所在目录
BASE_DIR = Path(__file__).resolve().parent

# 2. 指定 CSV 文件路径
csv_path = BASE_DIR / "data" / "results.csv"

# 3. 读取 CSV 文件
df = pd.read_csv(csv_path)

# 4. 查看前 5 行
print("===== 数据预览 =====")
print(df.head())

# 5. 查看数据形状
print("\n===== shape =====")
print(df.shape)

# 6. 查看每一列的数据类型
print("\n===== dtypes =====")
print(df.dtypes)

# 7. 计算所有实验的 IGD 均值和标准差
print("\n===== IGD 基础统计 =====")
print("IGD mean:", df["igd"].mean())
print("IGD std:", df["igd"].std())

# 8. 按算法分组，分别计算统计量
print("\n===== 按算法分组 =====")
result = df.groupby("algorithm")["igd"].agg(["mean", "std"])
print(result)

# 9. 按算法统计多个科研指标
print("\n===== 多指标科研统计 =====")

summary = df.groupby("algorithm").agg(
    runs=("run", "count"),
    igd_mean=("igd", "mean"),
    igd_std=("igd", "std"),
    hv_mean=("hv", "mean"),
    hv_std=("hv", "std"),
    runtime_mean=("runtime_s", "mean"),
    runtime_std=("runtime_s", "std")
)

# 保留4位小数
summary = summary.round(4)

# 显示统计结果
print(summary.to_string())

# 10. 自动导出统计结果

output_dir = BASE_DIR / "output"

# 如果文件夹不存在，就自动创建
output_dir.mkdir(parents=True, exist_ok=True)

# 指定输出文件
output_file = output_dir / "summary.csv"

# 保存为CSV，保留算法名称这一列
summary.to_csv(
    output_file,
    encoding="utf-8-sig",
    index=True
)

print("\n===== 文件导出成功 =====")
print("保存位置：", output_file)


# 11. 定义科研绘图函数
def plot_metric(summary, metric, ylabel, filename):

    # 创建画布和坐标轴
    fig, ax = plt.subplots(figsize=(8, 5))

    # 根据指标名称获取均值和标准差
    means = summary[f"{metric}_mean"]
    stds = summary[f"{metric}_std"]

    # 绘制带误差棒的柱状图
    ax.bar(
        summary.index,
        means,
        yerr=stds,
        capsize=5
    )

    # 设置标题和坐标轴
    ax.set_title(f"{metric.upper()} Comparison")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel(ylabel)

    # 添加网格
    ax.grid(axis="y", alpha=0.3)

    # 调整布局
    fig.tight_layout()

    # 保存图片
    save_path = output_dir / filename
    fig.savefig(save_path, dpi=300)

    # 释放画布
    plt.close(fig)

    print("图片已生成：", save_path)


# 12. 分别绘制三种指标

plot_metric(
    summary,
    "igd",
    "Mean IGD (Lower is Better)",
    "igd_comparison.png"
)

plot_metric(
    summary,
    "hv",
    "Mean HV (Higher is Better)",
    "hv_comparison.png"
)

plot_metric(
    summary,
    "runtime",
    "Runtime (seconds)",
    "runtime_comparison.png"
)


from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ===== 1. 设置文件路径 =====

base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "output"

summary_path = output_dir / "algorithm_summary.csv"


# ===== 2. 读取统计数据 =====

df = pd.read_csv(summary_path)

print("===== 算法统计数据 =====")
print(df.head())

print("\n数据形状：", df.shape)


# ===== 3. 设置算法和测试函数顺序 =====

algorithms = ["NSGA-II", "MOEA/D", "NSGA-III"]
problems = ["DTLZ1", "DTLZ2", "DTLZ3"]


# ===== 4. 定义通用绘图函数 =====

def plot_comparison(
    metric,
    std_metric,
    ylabel,
    filename
):

    # 将长表转换成适合绘图的矩阵
    mean_table = df.pivot(
        index="problem",
        columns="algorithm",
        values=metric
    )

    std_table = df.pivot(
        index="problem",
        columns="algorithm",
        values=std_metric
    )

    # 固定行列顺序
    mean_table = mean_table.reindex(
        index=problems,
        columns=algorithms
    )

    std_table = std_table.reindex(
        index=problems,
        columns=algorithms
    )

    # 横坐标位置
    x = np.arange(len(problems))

    # 每个柱子的宽度
    width = 0.25

    fig, ax = plt.subplots(figsize=(9, 5))

    # 绘制三个算法的柱状图
    for i, algorithm in enumerate(algorithms):

        positions = x + (i - 1) * width

        means = mean_table[algorithm].to_numpy()
        stds = std_table[algorithm].to_numpy()

        ax.bar(
            positions,
            means,
            width,
            yerr=stds,
            capsize=4,
            label=algorithm
        )

    # 设置标题与坐标轴
    ax.set_title(f"{metric.upper()} Comparison")
    ax.set_xlabel("Test Problem")
    ax.set_ylabel(ylabel)

    ax.set_xticks(x)
    ax.set_xticklabels(problems)

    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    # 保存高清图片
    save_path = output_dir / filename
    fig.savefig(save_path, dpi=300)

    plt.close(fig)

    print("图片已保存：", save_path)


# ===== 5. 绘制 IGD 对比图 =====

plot_comparison(
    metric="igd_mean",
    std_metric="igd_std",
    ylabel="IGD (Lower is Better)",
    filename="igd_comparison.png"
)


# ===== 6. 绘制 HV 对比图 =====

plot_comparison(
    metric="hv_mean",
    std_metric="hv_std",
    ylabel="HV (Higher is Better)",
    filename="hv_comparison.png"
)


print("\n===== 绘图完成 =====")

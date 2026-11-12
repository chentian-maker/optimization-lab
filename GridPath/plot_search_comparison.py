
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# =====================================
# 1. 读取实验数据
# =====================================

df = pd.read_csv(
    "comparison_results.csv",
    encoding="utf-8-sig"
)

# 检查必要字段
required_columns = [
    "algorithm",
    "discovered_count",
    "expanded_count",
    "processed_count",
    "path_length",
    "runtime_ms",
    "guarantees_shortest",
    "is_shortest_this_run",
    "optimal_path_length"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"实验数据缺少字段：{missing_columns}")

# 中文字体
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei"
]

plt.rcParams["axes.unicode_minus"] = False


print("===== 实验数据预览 =====")

print(df[required_columns].to_string(index=False))


# =====================================
# 2. 输出算法最优性评价
# =====================================

print("\n===== 算法最优性评价 =====")

for _, row in df.iterrows():

    print(f"\n算法：{row['algorithm']}")

    print(
        "理论保证最短路径：",
        "是" if bool(row["guarantees_shortest"]) else "否"
    )

    print(
        "本次结果是否最短：",
        "是" if bool(row["is_shortest_this_run"]) else "否"
    )

    print("本次路径长度：", row["path_length"])

    print("理论最短路径长度：", row["optimal_path_length"])


# =====================================
# 3. 图一：节点数量对比
# =====================================

fig, ax = plt.subplots(figsize=(9, 5))

x = np.arange(len(df))

width = 0.25

ax.bar(
    x - width,
    df["discovered_count"],
    width,
    label="发现节点"
)

ax.bar(
    x,
    df["expanded_count"],
    width,
    label="展开节点"
)

ax.bar(
    x + width,
    df["processed_count"],
    width,
    label="处理节点"
)

ax.set_xticks(x)

ax.set_xticklabels(df["algorithm"])

ax.set_title("BFS 与 DFS 节点数量对比")

ax.set_ylabel("节点数量")

ax.set_xlabel("搜索算法")

ax.legend()

ax.grid(axis="y", alpha=0.3)

fig.tight_layout()

fig.savefig(
    "search_node_comparison.png",
    dpi=200
)

plt.close(fig)


# =====================================
# 4. 图二：路径长度与最优性对比
# =====================================

fig, ax = plt.subplots(figsize=(9, 5))

valid_df = df[df["path_length"].notna()].copy()

bars = ax.bar(
    valid_df["algorithm"],
    valid_df["path_length"],
    label="实际路径长度"
)

# 最短路径基准
optimal_values = df["optimal_path_length"].dropna()

if not optimal_values.empty:

    optimal_length = optimal_values.iloc[0]

    ax.axhline(
        y=optimal_length,
        linestyle="--",
        linewidth=2,
        label=f"最短路径基准：{optimal_length}"
    )

# 在柱状图上显示路径长度
for bar in bars:

    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom"
    )

ax.set_title("BFS 与 DFS 路径长度及最优性对比")

ax.set_ylabel("路径长度（边数）")

ax.set_xlabel("搜索算法")

ax.legend()

ax.grid(axis="y", alpha=0.3)

fig.tight_layout()

fig.savefig(
    "path_length_comparison.png",
    dpi=200
)

plt.close(fig)


# =====================================
# 5. 图三：运行时间对比
# =====================================

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(
    df["algorithm"],
    df["runtime_ms"]
)

for bar in bars:

    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.6f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("BFS 与 DFS 平均运行时间对比")

ax.set_ylabel("平均运行时间（ms）")

ax.set_xlabel("搜索算法")

ax.grid(axis="y", alpha=0.3)

fig.tight_layout()

fig.savefig(
    "runtime_comparison.png",
    dpi=200
)

plt.close(fig)


# =====================================
# 6. 输出完成信息
# =====================================

print("\n===== 图表生成完成 =====")

print("1. search_node_comparison.png")

print("2. path_length_comparison.png")

print("3. runtime_comparison.png")

print("\n===== 算法实验分析完成 =====")

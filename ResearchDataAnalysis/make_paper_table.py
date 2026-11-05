
from pathlib import Path
import pandas as pd


# ===== 1. 设置文件路径 =====

base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "output"

input_path = output_dir / "algorithm_summary.csv"


# ===== 2. 读取实验统计数据 =====

df = pd.read_csv(input_path)

print("===== 原始统计数据 =====")
print(df.head())


# ===== 3. 固定表格中的显示顺序 =====

algorithms = ["NSGA-II", "MOEA/D", "NSGA-III"]
problems = ["DTLZ1", "DTLZ2", "DTLZ3"]

df["algorithm"] = pd.Categorical(
    df["algorithm"],
    categories=algorithms,
    ordered=True
)

df["problem"] = pd.Categorical(
    df["problem"],
    categories=problems,
    ordered=True
)

df = df.sort_values(["problem", "algorithm"])


# ===== 4. 创建论文表格 =====

csv_rows = []
md_rows = []

for problem in problems:

    # 取出当前测试函数的实验结果
    group = df[df["problem"] == problem]

    # 找出当前测试函数的最佳均值
    best_igd = group["igd_mean"].min()
    best_hv = group["hv_mean"].max()

    for _, row in group.iterrows():

        # 格式化均值与标准差
        igd_text = (
            f"{row['igd_mean']:.4f} ± "
            f"{row['igd_std']:.4f}"
        )

        hv_text = (
            f"{row['hv_mean']:.4f} ± "
            f"{row['hv_std']:.4f}"
        )

        # Markdown 表格中加粗最佳结果
        md_igd = igd_text
        md_hv = hv_text

        if row["igd_mean"] == best_igd:
            md_igd = f"**{igd_text}**"

        if row["hv_mean"] == best_hv:
            md_hv = f"**{hv_text}**"

        # 普通 CSV 记录
        csv_rows.append({
            "problem": problem,
            "algorithm": str(row["algorithm"]),
            "runs": int(row["runs"]),
            "IGD (Mean ± Std)": igd_text,
            "HV (Mean ± Std)": hv_text,
            "Runtime Mean (s)": round(
                row["runtime_mean"], 4
            )
        })

        # Markdown 表格记录
        md_rows.append(
            f"| {problem} "
            f"| {row['algorithm']} "
            f"| {int(row['runs'])} "
            f"| {md_igd} "
            f"| {md_hv} "
            f"| {row['runtime_mean']:.4f} |"
        )


# ===== 5. 保存 CSV 表格 =====

csv_path = output_dir / "paper_table.csv"

pd.DataFrame(csv_rows).to_csv(
    csv_path,
    index=False,
    encoding="utf-8-sig"
)


# ===== 6. 保存 Markdown 表格 =====

md_path = output_dir / "paper_table.md"

header = [
    "# Multi-objective Optimization Results",
    "",
    "> Synthetic data for learning only.",
    "> Not real algorithm benchmark results.",
    "",
    "| Problem | Algorithm | Runs | IGD ↓ "
    "| HV ↑ | Runtime (s) ↓ |",
    "|---|---|---:|---:|---:|---:|"
]

table_text = "\n".join(
    header + md_rows
)

md_path.write_text(
    table_text,
    encoding="utf-8"
)


# ===== 7. 打印运行结果 =====

print("\n===== 论文表格生成成功 =====")
print("CSV 文件：", csv_path)
print("Markdown 文件：", md_path)
print("表格数据行数：", len(csv_rows))

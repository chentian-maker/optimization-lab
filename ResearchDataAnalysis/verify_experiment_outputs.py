
from pathlib import Path
import pandas as pd


# ===== 1. 设置文件路径 =====

base_dir = Path(__file__).resolve().parent

data_dir = base_dir / "data"
output_dir = base_dir / "output"


# ===== 2. 加载实验数据 =====

raw = pd.read_csv(
    data_dir / "multi_algorithm_results.csv"
)

clean = pd.read_csv(
    output_dir / "clean_results.csv"
)

invalid = pd.read_csv(
    output_dir / "invalid_results.csv"
)

summary = pd.read_csv(
    output_dir / "algorithm_summary.csv"
)

paper = pd.read_csv(
    output_dir / "paper_table.csv"
)


# ===== 3. 检查数据数量 =====

assert len(raw) == 90, "原始记录数不正确"

assert len(clean) == 87, "有效记录数不正确"

assert len(invalid) == 3, "异常记录数不正确"

print("[PASS] 数据数量检查")


# ===== 4. 检查清洗后的数据 =====

assert not clean[
    ["igd", "hv", "runtime_s"]
].isna().any().any(), "仍然存在缺失值"

assert (clean["igd"] >= 0).all(), "IGD 存在负数"

assert clean["hv"].between(0, 1).all(), "HV 超出模拟范围"

assert (clean["runtime_s"] > 0).all(), "运行时间异常"

print("[PASS] 数据清洗检查")


# ===== 5. 检查统计表 =====

assert len(summary) == 9, "统计组数不正确"

assert summary["runs"].sum() == 87, "统计次数不正确"

assert len(paper) == 9, "论文表格行数不正确"

print("[PASS] 统计表检查")


# ===== 6. 检查科研图表 =====

figures = [
    "igd_comparison.png",
    "hv_comparison.png"
]

for filename in figures:

    path = output_dir / filename

    assert path.exists(), f"图片不存在：{filename}"

    assert path.stat().st_size > 0, f"图片为空：{filename}"

print("[PASS] 科研图片文件检查")


# ===== 7. 检查 Markdown 表格 =====

markdown_path = output_dir / "paper_table.md"

assert markdown_path.exists(), "Markdown 表格不存在"

markdown_text = markdown_path.read_text(
    encoding="utf-8"
)

assert "NSGA-III" in markdown_text, "缺少算法名称"

assert "**" in markdown_text, "缺少最佳结果标记"

print("[PASS] Markdown 表格检查")


print("\n===== 全部测试通过 =====")

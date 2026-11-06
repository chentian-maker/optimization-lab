
import csv
import numpy as np
from scipy.stats import wilcoxon

# 第1步：读取30次实验的数据
data = {}

with open("multi_seed_details.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        gen = int(row["Generations"])
        seed = int(row["Seed"])

        data[(gen, seed)] = {
            "IGD": float(row["IGD"]),
            "HV": float(row["HV"])
        }

# 第2步：按照相同随机种子进行配对
seeds = range(1, 11)

for metric in ["IGD", "HV"]:

    values_100 = np.array([
        data[(100, seed)][metric]
        for seed in seeds
    ])

    values_200 = np.array([
        data[(200, seed)][metric]
        for seed in seeds
    ])

    # IGD 越小越好，HV 越大越好
    if metric == "IGD":
        improvement = values_100 - values_200
    else:
        improvement = values_200 - values_100

    # 第3步：进行双侧 Wilcoxon 配对检验
    result = wilcoxon(
        improvement,
        alternative="two-sided",
        method="auto"
    )

    # 第4步：输出结果
    print(f"\n===== {metric} =====")
    print("Mean (100):", f"{values_100.mean():.6f}")
    print("Mean (200):", f"{values_200.mean():.6f}")
    print("Improved seeds:", np.sum(improvement > 0))
    print("Wilcoxon statistic:", result.statistic)
    print("p-value:", f"{result.pvalue:.6f}")

    if result.pvalue < 0.025:
        print("Significant (Bonferroni threshold 0.025)")
    else:
        print("Not significant at corrected threshold")


import csv
from statistics import mean, stdev

import numpy as np

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV

# 第1步：创建实验问题
problem = get_problem("zdt1")

# 第2步：创建理论参考前沿
f1 = np.linspace(0, 1, 1001)
pf = np.column_stack((f1, 1 - np.sqrt(f1)))

# 第3步：建立指标计算器
igd = IGD(pf)
hv = HV(ref_point=np.array([1.1, 1.1]))

# 第4步：设置实验条件
generations = [50, 100, 200]
seeds = range(1, 11)

all_results = []

# 第5步：重复运行 NSGA-II
for n_gen in generations:
    print(f"\n===== Generations: {n_gen} =====")

    for seed in seeds:

        algorithm = NSGA2(pop_size=100)

        res = minimize(
            problem,
            algorithm,
            ("n_gen", n_gen),
            seed=seed,
            verbose=False
        )

        igd_value = float(igd(res.F))
        hv_value = float(hv(res.F))

        all_results.append([
            n_gen,
            seed,
            igd_value,
            hv_value
        ])

        print(
            f"Seed {seed:2d}: "
            f"IGD={igd_value:.6f}, "
            f"HV={hv_value:.6f}",
            flush=True
        )

# 第6步：保存每次实验的原始结果
with open(
    "multi_seed_details.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerow([
        "Generations", "Seed", "IGD", "HV"
    ])
    writer.writerows(all_results)

# 第7步：计算均值和样本标准差
summary_results = []

print("\n===== Statistical Summary =====")

for n_gen in generations:

    rows = [
        row for row in all_results
        if row[0] == n_gen
    ]

    igd_values = [row[2] for row in rows]
    hv_values = [row[3] for row in rows]

    igd_mean = mean(igd_values)
    igd_std = stdev(igd_values)

    hv_mean = mean(hv_values)
    hv_std = stdev(hv_values)

    summary_results.append([
        n_gen,
        igd_mean,
        igd_std,
        hv_mean,
        hv_std
    ])

    print(f"\nGenerations: {n_gen}")
    print(f"IGD: {igd_mean:.6f} +/- {igd_std:.6f}")
    print(f"HV:  {hv_mean:.6f} +/- {hv_std:.6f}")

# 第8步：保存统计汇总
with open(
    "multi_seed_summary.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerow([
        "Generations",
        "IGD_Mean",
        "IGD_Std",
        "HV_Mean",
        "HV_Std"
    ])
    writer.writerows(summary_results)

print("\nAll experiments completed!")
print("Saved: multi_seed_details.csv")
print("Saved: multi_seed_summary.csv")

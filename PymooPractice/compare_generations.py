
import numpy as np
import csv

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV

# 创建问题和理论参考前沿
problem = get_problem("zdt1")
f1 = np.linspace(0, 1, 1001)
pf = np.column_stack((f1, 1 - np.sqrt(f1)))

# 创建评价指标
igd = IGD(pf)
hv = HV(ref_point=np.array([1.1, 1.1]))

# 对比不同迭代代数
generations = [50, 100, 200]
results = []

for n_gen in generations:

    algorithm = NSGA2(pop_size=100)

    res = minimize(
        problem,
        algorithm,
        ("n_gen", n_gen),
        seed=1,
        verbose=False
    )

    igd_value = igd(res.F)
    hv_value = hv(res.F)

    results.append([n_gen, igd_value, hv_value])

    print(f"Generations: {n_gen}")
    print(f"IGD: {igd_value:.6f}")
    print(f"HV:  {hv_value:.6f}")
    print("------------------------")

# 保存实验对比结果
with open(
    "generation_comparison.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerow(["Generations", "IGD", "HV"])
    writer.writerows(results)

print("Comparison saved successfully!")


import numpy as np
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV

# 1. 读取 NSGA-II 求出的解
F = np.loadtxt(
    "nsga2_results.csv",
    delimiter=",",
    skiprows=1
)

# 2. 创建 ZDT1 理论 Pareto 前沿的参考点
f1 = np.linspace(0, 1, 1001)
f2 = 1 - np.sqrt(f1)
pf = np.column_stack((f1, f2))

# 3. 计算 IGD（越小越好）
igd_value = IGD(pf)(F)

# 4. 计算 HV（越大越好）
ref_point = np.array([1.1, 1.1])
hv_value = HV(ref_point=ref_point)(F)

# 5. 计算参考前沿的近似 HV
hv_reference = HV(ref_point=ref_point)(pf)

# 6. 输出评价结果
print("===== NSGA-II Evaluation =====")
print(f"IGD: {igd_value:.6f}")
print(f"HV: {hv_value:.6f}")
print(f"Reference HV: {hv_reference:.6f}")

# 7. 保存评价结果
with open("evaluation.txt", "w", encoding="utf-8") as file:
    file.write(f"IGD: {igd_value:.6f}\n")
    file.write(f"HV: {hv_value:.6f}\n")
    file.write(f"Reference HV: {hv_reference:.6f}\n")

print("Evaluation saved to evaluation.txt")

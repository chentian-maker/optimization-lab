
import numpy as np
import matplotlib.pyplot as plt
from pymoo.problems import get_problem

# 1. 读取刚才保存的实验结果
F = np.loadtxt(
    "nsga2_results.csv",
    delimiter=",",
    skiprows=1
)

# 2. 获得 ZDT1 的理论 Pareto 前沿
problem = get_problem("zdt1")
pf = problem.pareto_front()

# 3. 创建画布
plt.figure(figsize=(8, 6))

# 4. 绘制理论最优曲线
plt.plot(
    pf[:, 0],
    pf[:, 1],
    "k-",
    linewidth=2,
    label="True Pareto Front"
)

# 5. 绘制算法得到的解
plt.scatter(
    F[:, 0],
    F[:, 1],
    color="red",
    s=25,
    label="NSGA-II Solutions"
)

# 6. 设置图表信息
plt.xlabel("Objective f1")
plt.ylabel("Objective f2")
plt.title("NSGA-II on ZDT1")
plt.legend()
plt.grid(True, alpha=0.3)

# 7. 保存图像
plt.tight_layout()
plt.savefig("pareto_comparison.png", dpi=200)
plt.close()

print("Plot saved: pareto_comparison.png")
print("Number of solutions:", len(F))

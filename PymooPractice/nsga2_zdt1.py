
# 第一次 NSGA-II 多目标优化实验
# 测试问题：ZDT1

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

# 第1步：创建测试问题
problem = get_problem("zdt1")

# 第2步：创建 NSGA-II 算法
algorithm = NSGA2(pop_size=100)

# 第3步：开始优化
result = minimize(
    problem,
    algorithm,
    ("n_gen", 200),
    seed=1,
    verbose=False
)

# 第4步：获取优化结果
F = result.F

# 第5步：打印结果
print("===== NSGA-II Experiment =====")
print("Problem: ZDT1")
print("Population size: 100")
print("Generations: 200")
print("Number of solutions:", len(F))

print("\nFirst 5 solutions:")
print(F[:5])

# 第6步：保存目标函数值
np.savetxt(
    "nsga2_results.csv",
    F,
    delimiter=",",
    header="f1,f2",
    comments=""
)

print("\nResults saved to nsga2_results.csv")

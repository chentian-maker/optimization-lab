
from optimization_lab.problems.base import Problem
from optimization_lab.problems.zdt1 import ZDT1
from optimization_lab.problems.zdt2 import ZDT2


# 这个函数不关心具体是哪一种优化问题
def evaluate_problem(problem: Problem, x):

    result = problem.evaluate(x)

    return result


# 创建两个不同的优化问题
problems = [
    ZDT1(),
    ZDT2()
]

# 准备相同的决策变量
x = [0.5] * 30


# 使用同一个函数计算两个问题
for problem in problems:

    result = evaluate_problem(problem, x)

    print(f"问题名称：{problem.__class__.__name__}")
    print(f"目标函数值：{result}")
    print("-" * 40)


import math


def zdt1(x):
    """
    ZDT1 双目标优化问题

    输入：
        x：30维决策变量，每个变量范围为[0, 1]

    输出：
        f1：第一个目标函数
        f2：第二个目标函数
    """

    # 检查决策变量数量
    if len(x) < 2:
        raise ValueError("决策变量数量至少为2")

    # 检查变量范围
    for value in x:
        if not 0.0 <= value <= 1.0:
            raise ValueError("决策变量必须在[0, 1]范围内")

    # 第一个目标函数
    f1 = x[0]

    # 计算辅助函数g
    n = len(x)

    g = 1.0 + 9.0 * sum(x[1:]) / (n - 1)

    # 第二个目标函数
    f2 = g * (1.0 - math.sqrt(f1 / g))

    return f1, f2


if __name__ == "__main__":

    # 测试1：理论Pareto最优解
    x1 = [0.5] + [0.0] * 29

    # 测试2：另一个理论Pareto最优解
    x2 = [0.25] + [0.0] * 29

    # 测试3：非Pareto最优解
    x3 = [0.5] + [1.0] * 29

    test_cases = [
        ("测试1", x1),
        ("测试2", x2),
        ("测试3", x3)
    ]

    for name, x in test_cases:
        f1, f2 = zdt1(x)

        print(name)
        print("决策变量数量：", len(x))
        print(f"f1 = {f1:.6f}")
        print(f"f2 = {f2:.6f}")
        print()

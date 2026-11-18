
from optimization_lab.problems.base import Problem


class ZDT1(Problem):

    def __init__(self, n_var=30):

        if n_var < 2:
            raise ValueError("ZDT1 requires at least 2 variables.")

        # 调用父类的初始化方法
        super().__init__(
            n_var=n_var,
            n_obj=2,
            xl=0.0,
            xu=1.0
        )

    def evaluate(self, x):

        if len(x) != self.n_var:
            raise ValueError("Incorrect number of decision variables.")

        if any(value < self.xl or value > self.xu for value in x):
            raise ValueError("Decision variables must be in [0, 1].")

        f1 = x[0]

        g = 1 + 9 * sum(x[1:]) / (self.n_var - 1)

        f2 = g * (1 - (f1 / g) ** 0.5)

        return f1, f2


# 兼容旧代码
def zdt1(x):
    problem = ZDT1(n_var=len(x))
    return problem.evaluate(x)

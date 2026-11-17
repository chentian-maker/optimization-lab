
class ZDT1:

    def __init__(self, n_var=30):

        if n_var < 2:
            raise ValueError("ZDT1 requires at least 2 variables.")

        self.n_var = n_var
        self.n_obj = 2

        self.xl = 0.0
        self.xu = 1.0

    def evaluate(self, x):

        if len(x) != self.n_var:
            raise ValueError("Incorrect number of decision variables.")

        if any(value < self.xl or value > self.xu for value in x):
            raise ValueError("Decision variables must be in [0, 1].")

        f1 = x[0]

        g = 1 + 9 * sum(x[1:]) / (self.n_var - 1)

        f2 = g * (1 - (f1 / g) ** 0.5)

        return f1, f2


# 保留原来的函数接口，兼容旧代码
def zdt1(x):
    problem = ZDT1(n_var=len(x))
    return problem.evaluate(x)

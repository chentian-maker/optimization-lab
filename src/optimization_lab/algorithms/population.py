
import numpy as np


class Population:
    """多目标优化算法的种群管理类。"""

    def __init__(self, X):

        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("种群必须是二维矩阵")

        if X.shape[0] == 0 or X.shape[1] == 0:
            raise ValueError("种群不能为空")

        if not np.all(np.isfinite(X)):
            raise ValueError("决策变量必须是有限数值")

        self.X = X.copy()
        self.F = None
        self.rank = None
        self.crowding_distance = None

    def evaluate(self, problem):

        if self.n_var != problem.n_var:
            raise ValueError(
                f"决策变量数量不匹配："
                f"种群有 {self.n_var} 个，"
                f"问题要求 {problem.n_var} 个"
            )

        results = [
            problem.evaluate(x)
            for x in self.X
        ]

        F = np.asarray(results, dtype=float)

        if F.shape != (self.n_pop, problem.n_obj):
            raise ValueError("目标函数评价结果形状不正确")

        if not np.all(np.isfinite(F)):
            raise ValueError("目标函数结果包含非有限数值")

        self.F = F

        return self.F

    @property
    def n_pop(self):
        return self.X.shape[0]

    @property
    def n_var(self):
        return self.X.shape[1]

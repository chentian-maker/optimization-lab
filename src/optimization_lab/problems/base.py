
from abc import ABC, abstractmethod


class Problem(ABC):
    """
    多目标优化问题的基础抽象类。

    所有具体优化问题都应该继承 Problem，
    并实现 evaluate() 方法。
    """

    def __init__(self, n_var, n_obj, xl, xu):

        self.n_var = n_var
        self.n_obj = n_obj

        self.xl = xl
        self.xu = xu

    @abstractmethod
    def evaluate(self, x):
        """
        计算给定决策变量对应的目标函数值。

        子类必须实现这个方法。
        """
        pass

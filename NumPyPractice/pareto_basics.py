
import numpy as np


def dominates(a, b):
    """判断最小化问题中，方案 a 是否 Pareto 支配方案 b。"""

    a = np.asarray(a)
    b = np.asarray(b)

    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("目标值必须是一维数组")

    if a.shape != b.shape or a.size == 0:
        raise ValueError("目标维度必须相同且不能为空")

    not_worse = np.all(a <= b)
    strictly_better = np.any(a < b)

    return bool(not_worse and strictly_better)


def main():
    A = np.array([100, 50])
    B = np.array([120, 40])
    C = np.array([90, 65])
    D = np.array([110, 45])
    E = np.array([130, 70])

    print("===== Pareto 支配关系测试 =====")

    print("A 支配 B:", dominates(A, B))
    print("A 支配 C:", dominates(A, C))
    print("A 支配 D:", dominates(A, D))
    print("D 支配 A:", dominates(D, A))
    print("A 支配 E:", dominates(A, E))
    print("B 支配 E:", dominates(B, E))


if __name__ == "__main__":
    main()

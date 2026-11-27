"""Mutation operators for evolutionary algorithms."""

import numpy as np


def polynomial_mutation(
    x,
    xl=0.0,
    xu=1.0,
    eta=20.0,
    prob=None,
    rng=None
):
    """Perform bounded polynomial mutation."""

    if rng is None:
        rng = np.random.default_rng()

    # 转换并复制个体
    child = np.asarray(x, dtype=float).copy()

    # 检查个体维度
    if child.ndim != 1 or child.size == 0:
        raise ValueError(
            "Individual must be a non-empty 1D array."
        )

    if not np.all(np.isfinite(child)):
        raise ValueError("Individual must be finite.")

    n_var = child.size

    # 默认单变量变异概率
    if prob is None:
        prob = 1.0 / n_var

    # 检查参数
    if not np.isfinite(eta) or eta < 0:
        raise ValueError(
            "eta must be finite and non-negative."
        )

    if not 0 <= prob <= 1:
        raise ValueError(
            "prob must be between 0 and 1."
        )

    # 将上下界广播为数组
    xl = np.broadcast_to(
        np.asarray(xl, dtype=float),
        child.shape
    )

    xu = np.broadcast_to(
        np.asarray(xu, dtype=float),
        child.shape
    )

    # 检查上下界
    if not np.all(np.isfinite(xl)):
        raise ValueError("Lower bounds must be finite.")

    if not np.all(np.isfinite(xu)):
        raise ValueError("Upper bounds must be finite.")

    if np.any(xl >= xu):
        raise ValueError(
            "Lower bounds must be smaller than upper bounds."
        )

    # 检查原始个体是否越界
    if np.any((child < xl) | (child > xu)):
        raise ValueError("Individual is out of bounds.")

    mut_pow = 1.0 / (eta + 1.0)

    # 对每个决策变量执行变异判断
    for i in range(n_var):

        if rng.random() >= prob:
            continue

        value = child[i]

        lower = xl[i]
        upper = xu[i]

        width = upper - lower

        # 计算归一化边界距离
        delta1 = (value - lower) / width
        delta2 = (upper - value) / width

        u = rng.random()

        if u <= 0.5:

            xy = 1.0 - delta1

            val = (
                2.0 * u
                + (1.0 - 2.0 * u)
                * xy ** (eta + 1.0)
            )

            deltaq = val ** mut_pow - 1.0

        else:

            xy = 1.0 - delta2

            val = (
                2.0 * (1.0 - u)
                + 2.0 * (u - 0.5)
                * xy ** (eta + 1.0)
            )

            deltaq = 1.0 - val ** mut_pow

        # 将归一化变异量转换为实际变异量
        child[i] = value + deltaq * width

    # 浮点数边界保护
    return np.clip(child, xl, xu)
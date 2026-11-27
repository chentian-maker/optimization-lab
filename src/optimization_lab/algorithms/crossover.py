"""Crossover operators for evolutionary algorithms."""

import numpy as np


def sbx_crossover(
    parent1,
    parent2,
    xl=0.0,
    xu=1.0,
    eta=20.0,
    prob=0.9,
    prob_var=0.5,
    rng=None
):
    """Perform bounded simulated binary crossover."""

    if rng is None:
        rng = np.random.default_rng()

    p1 = np.asarray(parent1, dtype=float)
    p2 = np.asarray(parent2, dtype=float)

    # 检查父代维度
    if p1.ndim != 1 or p2.ndim != 1:
        raise ValueError("Parents must be 1D arrays.")

    if p1.shape != p2.shape or p1.size == 0:
        raise ValueError("Invalid parent shapes.")

    if not np.all(np.isfinite(p1)) or not np.all(np.isfinite(p2)):
        raise ValueError("Parents must be finite.")

    # 检查交叉参数
    if not np.isfinite(eta) or eta < 0:
        raise ValueError("eta must be finite and non-negative.")

    if not 0 <= prob <= 1:
        raise ValueError("prob must be between 0 and 1.")

    if not 0 <= prob_var <= 1:
        raise ValueError("prob_var must be between 0 and 1.")

    # 将上下界扩展为数组
    xl = np.broadcast_to(
        np.asarray(xl, dtype=float),
        p1.shape
    )

    xu = np.broadcast_to(
        np.asarray(xu, dtype=float),
        p1.shape
    )

    if not np.all(np.isfinite(xl)) or not np.all(np.isfinite(xu)):
        raise ValueError("Bounds must be finite.")

    if np.any(xl >= xu):
        raise ValueError("Lower bounds must be smaller than upper bounds.")

    # 检查父代是否越界
    if np.any((p1 < xl) | (p1 > xu)):
        raise ValueError("Parent1 is out of bounds.")

    if np.any((p2 < xl) | (p2 > xu)):
        raise ValueError("Parent2 is out of bounds.")

    # 复制父代，保护原始数据
    child1 = p1.copy()
    child2 = p2.copy()

    # 判断是否执行交叉
    if rng.random() >= prob:
        return child1, child2

    exponent = 1.0 / (eta + 1.0)

    for i in range(len(p1)):

        # 判断当前变量是否交叉
        if rng.random() >= prob_var:
            continue

        # 两个变量相同时无需交叉
        if p1[i] == p2[i]:
            continue

        y1 = min(p1[i], p2[i])
        y2 = max(p1[i], p2[i])

        lower = xl[i]
        upper = xu[i]

        u = rng.random()

        # 计算靠近下边界的子代
        beta = 1.0 + 2.0 * (
            y1 - lower
        ) / (y2 - y1)

        alpha = 2.0 - beta ** (-(eta + 1.0))

        if u <= 1.0 / alpha:
            betaq = (u * alpha) ** exponent
        else:
            betaq = (
                1.0 / (2.0 - u * alpha)
            ) ** exponent

        c1 = 0.5 * (
            y1 + y2 - betaq * (y2 - y1)
        )

        # 计算靠近上边界的子代
        beta = 1.0 + 2.0 * (
            upper - y2
        ) / (y2 - y1)

        alpha = 2.0 - beta ** (-(eta + 1.0))

        if u <= 1.0 / alpha:
            betaq = (u * alpha) ** exponent
        else:
            betaq = (
                1.0 / (2.0 - u * alpha)
            ) ** exponent

        c2 = 0.5 * (
            y1 + y2 + betaq * (y2 - y1)
        )

        # 防止浮点计算导致越界
        c1 = np.clip(c1, lower, upper)
        c2 = np.clip(c2, lower, upper)

        # 随机分配给两个子代
        if rng.random() < 0.5:
            child1[i] = c2
            child2[i] = c1
        else:
            child1[i] = c1
            child2[i] = c2

    return child1, child2
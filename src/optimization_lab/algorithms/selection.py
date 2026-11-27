"""Selection operators for evolutionary algorithms."""

import numpy as np


def tournament_selection(
    ranks,
    crowding,
    n_select,
    rng=None
):
    """Select parent indices using binary tournaments."""

    if rng is None:
        rng = np.random.default_rng()

    ranks = np.asarray(ranks)
    crowding = np.asarray(crowding, dtype=float)

    # 检查输入数组维度
    if ranks.ndim != 1 or crowding.ndim != 1:
        raise ValueError("Inputs must be 1D arrays.")

    # 检查数组长度
    if len(ranks) != len(crowding):
        raise ValueError("Input lengths must match.")

    # 获取种群数量
    n_pop = len(ranks)

    if n_pop < 2:
        raise ValueError("Population must contain at least 2 individuals.")

    if not isinstance(n_select, (int, np.integer)) or n_select < 0:
        raise ValueError("n_select must be a non-negative integer.")

    if not np.all(np.isfinite(ranks)):
        raise ValueError("Ranks must be finite.")

    if np.any(np.isnan(crowding)):
        raise ValueError("Crowding distances cannot contain NaN.")

    # 创建用于保存父代下标的数组
    selected = np.empty(n_select, dtype=int)

    for k in range(n_select):

        # 随机选择两个不同的个体
        i, j = rng.choice(
            n_pop,
            size=2,
            replace=False
        )

        # 优先比较非支配等级
        if ranks[i] < ranks[j]:
            winner = i

        elif ranks[i] > ranks[j]:
            winner = j

        # 等级相同，比较拥挤距离
        elif crowding[i] > crowding[j]:
            winner = i

        elif crowding[i] < crowding[j]:
            winner = j

        # 完全相同，随机选择
        else:
            winner = rng.choice([i, j])

        selected[k] = winner

    return selected
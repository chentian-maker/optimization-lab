import numpy as np


def polynomial_mutation(x, eta=20, prob=None, rng=None):

    if rng is None:
        rng = np.random.default_rng()

    # 复制个体，避免修改原始数据
    child = np.asarray(x, dtype=float).copy()

    n_var = len(child)

    # 默认变异概率
    if prob is None:
        prob = 1.0 / n_var

    # 决策变量上下界
    xl = 0.0
    xu = 1.0

    for i in range(n_var):

        # 判断当前变量是否发生变异
        if rng.random() >= prob:
            continue

        value = child[i]

        # 计算与上下边界的距离
        delta1 = (value - xl) / (xu - xl)
        delta2 = (xu - value) / (xu - xl)

        # 生成变异随机数
        u = rng.random()

        mut_pow = 1.0 / (eta + 1.0)

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

        # 执行变异
        child[i] = value + deltaq * (xu - xl)

    # 边界保护
    return np.clip(child, xl, xu)


if __name__ == "__main__":

    rng = np.random.default_rng(42)

    parent = np.array([
        0.2, 0.4, 0.6, 0.8
    ])

    child = polynomial_mutation(
        parent,
        eta=20,
        prob=1.0,
        rng=rng
    )

    print("===== 多项式变异实验 =====")

    print("变异前：", parent)
    print("变异后：", child)

    print("变量变化量：", child - parent)

    print("发生变化的变量数量：",
          np.count_nonzero(child != parent))

    print("是否满足边界：",
          np.all((child >= 0) & (child <= 1)))
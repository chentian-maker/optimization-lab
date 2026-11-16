def zdt1(x):
    n = len(x)

    if n < 2:
        raise ValueError("ZDT1 requires at least 2 variables.")

    f1 = x[0]
    g = 1 + 9 * sum(x[1:]) / (n - 1)
    f2 = g * (1 - (f1 / g) ** 0.5)

    return f1, f2
def sphere(x):
    """Sphere 函数：f(x) = sum(x_i^2)"""
    return sum(xi * xi for xi in x)


if __name__ == "__main__":
    print(sphere([1.0, -2.0, 3.0]))  # 14.0

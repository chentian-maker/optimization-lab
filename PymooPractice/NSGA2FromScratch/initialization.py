
import random

from zdt1_problem import zdt1


def initialize_population(
    pop_size=100,
    n_var=30,
    lower=0.0,
    upper=1.0,
    seed=42
):
    """
    初始化 NSGA-II 种群。

    pop_size: 种群规模
    n_var: 决策变量数量
    lower: 决策变量下界
    upper: 决策变量上界
    seed: 随机种子
    """

    # 1. 检查输入参数
    if pop_size <= 0:
        raise ValueError("pop_size must be positive")

    if n_var < 2:
        raise ValueError("n_var must be at least 2")

    if lower >= upper:
        raise ValueError("lower must be smaller than upper")

    # 2. 创建随机数生成器
    rng = random.Random(seed)

    # 3. 创建空种群
    population = []

    # 4. 循环生成指定数量的个体
    for _ in range(pop_size):

        # 生成一个随机个体的决策变量
        x = [
            rng.uniform(lower, upper)
            for _ in range(n_var)
        ]

        # 5. 计算两个目标函数
        f1, f2 = zdt1(x)

        # 6. 创建完整个体
        individual = {
            "x": x,
            "f": (f1, f2),
            "rank": None,
            "crowding": 0.0
        }

        # 7. 将个体加入种群
        population.append(individual)

    return population


if __name__ == "__main__":

    # 初始化100个个体，每个个体有30个决策变量
    population = initialize_population(
        pop_size=100,
        n_var=30,
        seed=42
    )

    print("===== 种群初始化结果 =====")

    print("种群数量：", len(population))

    print("每个个体的决策变量数量：",
          len(population[0]["x"]))

    print("每个个体的目标数量：",
          len(population[0]["f"]))

    print("\n===== 前5个个体 =====")

    for i, individual in enumerate(population[:5], start=1):

        print(f"\n个体 {i}")

        print("决策变量前5个：",
              [round(v, 4) for v in individual["x"][:5]])

        print("目标函数值：",
              tuple(round(v, 6) for v in individual["f"]))

    # 8. 验证种群
    assert len(population) == 100

    assert all(
        len(individual["x"]) == 30
        for individual in population
    )

    assert all(
        len(individual["f"]) == 2
        for individual in population
    )

    assert all(
        0.0 <= v <= 1.0
        for individual in population
        for v in individual["x"]
    )

    # 9. 验证随机种子可复现
    population_again = initialize_population(
        pop_size=100,
        n_var=30,
        seed=42
    )

    assert population[0]["x"] == population_again[0]["x"]

    print("\n[PASS] 种群数量检查通过")
    print("[PASS] 决策变量维度检查通过")
    print("[PASS] 目标函数数量检查通过")
    print("[PASS] 变量边界检查通过")
    print("[PASS] 随机种子复现检查通过")

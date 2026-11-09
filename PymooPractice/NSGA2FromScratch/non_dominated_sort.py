
from initialization import initialize_population


# 判断个体 A 是否支配个体 B
def dominates(f_a, f_b):

    if len(f_a) != len(f_b):
        raise ValueError("目标函数维度不一致")

    # A 的所有目标都不比 B 差
    no_worse = all(
        a <= b for a, b in zip(f_a, f_b)
    )

    # A 至少有一个目标严格优于 B
    strictly_better = any(
        a < b for a, b in zip(f_a, f_b)
    )

    return no_worse and strictly_better


# 快速非支配排序
def fast_non_dominated_sort(population):

    n = len(population)

    if n == 0:
        return []

    # 每个个体支配的其他个体
    dominated_solutions = [[] for _ in range(n)]

    # 每个个体被多少个其他个体支配
    domination_count = [0] * n

    # 第一非支配层
    fronts = [[]]

    # 第一步：计算支配关系
    for p in range(n):

        for q in range(n):

            if p == q:
                continue

            f_p = population[p]["f"]
            f_q = population[q]["f"]

            if dominates(f_p, f_q):
                dominated_solutions[p].append(q)

            elif dominates(f_q, f_p):
                domination_count[p] += 1

        # 没有其他个体支配 p
        if domination_count[p] == 0:
            population[p]["rank"] = 0
            fronts[0].append(p)

    # 第二步：逐层生成后续非支配层
    i = 0

    while i < len(fronts):

        next_front = []

        for p in fronts[i]:

            for q in dominated_solutions[p]:

                domination_count[q] -= 1

                if domination_count[q] == 0:
                    population[q]["rank"] = i + 1
                    next_front.append(q)

        if next_front:
            fronts.append(next_front)

        i += 1

    return fronts


# 创建手工测试个体
def make_individual(name, f):

    return {
        "name": name,
        "f": f,
        "rank": None,
        "crowding": 0.0
    }


# 测试一：8个手工构造的个体
def test_eight_points():

    population = [
        make_individual("A", (1, 12)),
        make_individual("B", (3, 8)),
        make_individual("D", (5, 10)),
        make_individual("F", (8, 7)),
        make_individual("C", (5, 7)),
        make_individual("E", (6, 4)),
        make_individual("G", (10, 5)),
        make_individual("H", (9, 1))
    ]

    fronts = fast_non_dominated_sort(population)

    print("\n===== 8个个体排序测试 =====")

    actual = []

    for i, front in enumerate(fronts):
        names = [population[index]["name"] for index in front]
        actual.append(names)
        print(f"F{i + 1}: {names}")

    expected = [
        ["A", "B", "C", "E", "H"],
        ["D", "F", "G"]
    ]

    assert actual == expected

    print("[PASS] 8个个体排序正确")


# 测试二：100个ZDT1个体
def test_100_zdt1():

    population = initialize_population(
        pop_size=100,
        n_var=30,
        seed=42
    )

    fronts = fast_non_dominated_sort(population)

    all_indices = [
        index
        for front in fronts
        for index in front
    ]

    # 检查每个个体都被分配
    assert sorted(all_indices) == list(range(100))

    # 检查所有个体都有 Rank
    assert all(
        individual["rank"] is not None
        for individual in population
    )

    # 检查 Rank 与所属层级一致
    for rank, front in enumerate(fronts):
        assert all(
            population[index]["rank"] == rank
            for index in front
        )

    print("\n===== 100个ZDT1个体测试 =====")
    print("种群数量：", len(population))
    print("非支配层数量：", len(fronts))
    print("每层个体数量：", [len(f) for f in fronts])

    print("[PASS] 100个个体全部完成非支配排序")


if __name__ == "__main__":

    test_eight_points()

    test_100_zdt1()

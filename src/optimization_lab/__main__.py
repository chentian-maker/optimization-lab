
from optimization_lab.problems.zdt1 import ZDT1
from optimization_lab.problems.zdt2 import ZDT2


def main():
    print("=" * 50)
    print("Optimization-Lab v0.1")
    print("Multi-objective Optimization Research Platform")
    print("=" * 50)

    problems = [
        ZDT1(n_var=30),
        ZDT2(n_var=30),
    ]

    for problem in problems:
        x = [0.5] * problem.n_var

        f1, f2 = problem.evaluate(x)

        print(f"\nProblem: {problem.__class__.__name__}")
        print(f"Number of variables: {problem.n_var}")
        print(f"Number of objectives: {problem.n_obj}")
        print(f"Objective values: ({f1:.6f}, {f2:.6f})")

    print("\nAll problem demonstrations completed.")


if __name__ == "__main__":
    main()

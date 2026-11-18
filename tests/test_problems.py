
import unittest

from optimization_lab.problems.base import Problem
from optimization_lab.problems.zdt1 import ZDT1
from optimization_lab.problems.zdt2 import ZDT2


class TestProblems(unittest.TestCase):

    def test_inheritance(self):

        problems = [ZDT1(), ZDT2()]

        for problem in problems:
            self.assertIsInstance(problem, Problem)

    def test_common_attributes(self):

        problems = [ZDT1(), ZDT2()]

        for problem in problems:
            self.assertEqual(problem.n_var, 30)
            self.assertEqual(problem.n_obj, 2)
            self.assertEqual(problem.xl, 0.0)
            self.assertEqual(problem.xu, 1.0)

    def test_evaluate_output(self):

        problems = [ZDT1(), ZDT2()]
        x = [0.5] * 30

        for problem in problems:

            result = problem.evaluate(x)

            self.assertEqual(len(result), 2)

            self.assertTrue(
                all(isinstance(value, (int, float)) for value in result)
            )


if __name__ == "__main__":
    unittest.main()

import unittest

from optimization_lab.problems.base import Problem
from optimization_lab.problems.zdt1 import ZDT1


class TestAbstractProblem(unittest.TestCase):

    def test_cannot_create_problem_directly(self):

        with self.assertRaises(TypeError):
            Problem(30, 2, 0.0, 1.0)

    def test_zdt1_can_be_created(self):

        problem = ZDT1()

        self.assertIsInstance(problem, Problem)

    def test_zdt1_can_evaluate(self):

        problem = ZDT1()

        result = problem.evaluate([0.5] * 30)

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
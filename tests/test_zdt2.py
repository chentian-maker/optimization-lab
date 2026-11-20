
import unittest

from optimization_lab.problems.zdt2 import ZDT2


class TestZDT2(unittest.TestCase):

    def setUp(self):
        self.problem = ZDT2(n_var=30)

    def test_objective_values(self):

        x = [0.5] * 30

        f1, f2 = self.problem.evaluate(x)

        self.assertAlmostEqual(f1, 0.5)
        self.assertAlmostEqual(f2, 5.454545454545455)

    def test_invalid_variable_number(self):

        with self.assertRaises(ValueError):
            self.problem.evaluate([0.5] * 29)

    def test_out_of_bounds(self):

        x = [0.5] * 30
        x[0] = 1.5

        with self.assertRaises(ValueError):
            self.problem.evaluate(x)

    def test_number_of_objectives(self):

        self.assertEqual(self.problem.n_obj, 2)


if __name__ == "__main__":
    unittest.main()

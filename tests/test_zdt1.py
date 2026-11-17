
import unittest

from optimization_lab.problems.zdt1 import ZDT1, zdt1


class TestZDT1(unittest.TestCase):

    def setUp(self):
        self.problem = ZDT1(n_var=30)

    def test_objective_values(self):

        x = [0.5] * 30

        f1, f2 = self.problem.evaluate(x)

        self.assertAlmostEqual(f1, 0.5)
        self.assertAlmostEqual(f2, 3.8416876048223)

    def test_number_of_variables(self):

        self.assertEqual(self.problem.n_var, 30)

    def test_number_of_objectives(self):

        self.assertEqual(self.problem.n_obj, 2)

    def test_invalid_variable_number(self):

        with self.assertRaises(ValueError):
            self.problem.evaluate([0.5] * 29)

    def test_out_of_bounds(self):

        x = [0.5] * 30
        x[0] = 1.5

        with self.assertRaises(ValueError):
            self.problem.evaluate(x)

    def test_original_function(self):

        x = [0.5] * 30

        result = zdt1(x)

        self.assertAlmostEqual(result[0], 0.5)


if __name__ == "__main__":
    unittest.main()

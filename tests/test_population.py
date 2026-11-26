
import unittest
import numpy as np

from optimization_lab.algorithms import Population
from optimization_lab.problems.zdt1 import ZDT1


class TestPopulation(unittest.TestCase):

    def test_initialization(self):
        X = np.random.default_rng(42).random((100, 30))
        pop = Population(X)

        self.assertEqual(pop.n_pop, 100)
        self.assertEqual(pop.n_var, 30)
        self.assertIsNone(pop.F)

    def test_invalid_nan(self):
        X = np.ones((10, 30))
        X[0, 0] = np.nan

        with self.assertRaises(ValueError):
            Population(X)

    def test_empty_population(self):
        X = np.empty((0, 30))

        with self.assertRaises(ValueError):
            Population(X)

    def test_evaluation(self):
        problem = ZDT1(n_var=30)

        X = np.random.default_rng(42).random((100, 30))
        pop = Population(X)

        F = pop.evaluate(problem)

        self.assertEqual(F.shape, (100, 2))
        self.assertTrue(np.all(np.isfinite(F)))
        self.assertIs(pop.F, F)

    def test_variable_mismatch(self):
        problem = ZDT1(n_var=30)

        X = np.random.default_rng(42).random((10, 20))
        pop = Population(X)

        with self.assertRaises(ValueError):
            pop.evaluate(problem)


if __name__ == "__main__":
    unittest.main(verbosity=2)

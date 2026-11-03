
import unittest
import numpy as np

from pareto_basics import dominates


class TestParetoDominance(unittest.TestCase):

    def test_a_dominates_b(self):
        a = np.array([100, 50])
        b = np.array([130, 70])
        self.assertTrue(dominates(a, b))

    def test_tradeoff(self):
        a = np.array([100, 50])
        b = np.array([120, 40])
        self.assertFalse(dominates(a, b))
        self.assertFalse(dominates(b, a))

    def test_equal_solutions(self):
        a = np.array([100, 50])
        b = np.array([100, 50])
        self.assertFalse(dominates(a, b))

    def test_one_objective_equal(self):
        a = np.array([100, 50])
        b = np.array([100, 70])
        self.assertTrue(dominates(a, b))

    def test_three_objectives(self):
        a = np.array([10, 20, 30])
        b = np.array([15, 25, 35])
        self.assertTrue(dominates(a, b))

    def test_different_dimensions(self):
        a = np.array([100, 50])
        b = np.array([100, 50, 30])

        with self.assertRaises(ValueError):
            dominates(a, b)

    def test_empty_arrays(self):
        a = np.array([])
        b = np.array([])

        with self.assertRaises(ValueError):
            dominates(a, b)


if __name__ == "__main__":
    unittest.main()

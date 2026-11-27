import unittest
import numpy as np

from optimization_lab.algorithms import sbx_crossover


class TestCrossover(unittest.TestCase):

    def setUp(self):

        self.p1 = np.array([-3.0, 0.2, 6.0])
        self.p2 = np.array([3.0, 0.8, -6.0])

        self.xl = np.array([-5.0, 0.0, -10.0])
        self.xu = np.array([5.0, 1.0, 10.0])

        self.rng = np.random.default_rng(42)

    def test_output_shape(self):

        c1, c2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            rng=self.rng
        )

        self.assertEqual(c1.shape, (3,))
        self.assertEqual(c2.shape, (3,))

    def test_bounds(self):

        for _ in range(100):

            c1, c2 = sbx_crossover(
                self.p1, self.p2,
                xl=self.xl,
                xu=self.xu,
                prob=1.0,
                prob_var=1.0,
                rng=self.rng
            )

            self.assertTrue(
                np.all((c1 >= self.xl) & (c1 <= self.xu))
            )

            self.assertTrue(
                np.all((c2 >= self.xl) & (c2 <= self.xu))
            )

    def test_zero_probability(self):

        c1, c2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            prob=0.0,
            rng=self.rng
        )

        np.testing.assert_array_equal(c1, self.p1)
        np.testing.assert_array_equal(c2, self.p2)

    def test_zero_variable_probability(self):

        c1, c2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            prob_var=0.0,
            rng=self.rng
        )

        np.testing.assert_array_equal(c1, self.p1)
        np.testing.assert_array_equal(c2, self.p2)

    def test_identical_parents(self):

        c1, c2 = sbx_crossover(
            self.p1, self.p1,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            prob_var=1.0,
            rng=self.rng
        )

        np.testing.assert_array_equal(c1, self.p1)
        np.testing.assert_array_equal(c2, self.p1)

    def test_parents_unchanged(self):

        original1 = self.p1.copy()
        original2 = self.p2.copy()

        c1, c2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            prob_var=1.0,
            rng=self.rng
        )

        c1[0] = 0.0
        c2[0] = 0.0

        np.testing.assert_array_equal(
            self.p1, original1
        )

        np.testing.assert_array_equal(
            self.p2, original2
        )

    def test_invalid_shapes(self):

        with self.assertRaises(ValueError):

            sbx_crossover(
                [0.2, 0.4],
                [0.3]
            )

    def test_invalid_bounds(self):

        with self.assertRaises(ValueError):

            sbx_crossover(
                [0.2], [0.8],
                xl=1.0,
                xu=0.0
            )

    def test_invalid_probability(self):

        with self.assertRaises(ValueError):

            sbx_crossover(
                [0.2], [0.8],
                prob=1.5
            )

    def test_reproducibility(self):

        a1, a2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            prob_var=1.0,
            rng=np.random.default_rng(42)
        )

        b1, b2 = sbx_crossover(
            self.p1, self.p2,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            prob_var=1.0,
            rng=np.random.default_rng(42)
        )

        np.testing.assert_array_equal(a1, b1)
        np.testing.assert_array_equal(a2, b2)


if __name__ == "__main__":
    unittest.main()
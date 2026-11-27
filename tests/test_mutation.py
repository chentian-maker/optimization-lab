import unittest
import numpy as np

from optimization_lab.algorithms import polynomial_mutation


class TestMutation(unittest.TestCase):

    def setUp(self):

        self.parent = np.array([-3.0, 0.2, 6.0])

        self.xl = np.array([-5.0, 0.0, -10.0])
        self.xu = np.array([5.0, 1.0, 10.0])

        self.rng = np.random.default_rng(42)

    def test_output_shape(self):

        child = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            rng=self.rng
        )

        self.assertEqual(child.shape, (3,))

    def test_bounds(self):

        for _ in range(100):

            child = polynomial_mutation(
                self.parent,
                xl=self.xl,
                xu=self.xu,
                prob=1.0,
                rng=self.rng
            )

            self.assertTrue(
                np.all(
                    (child >= self.xl)
                    & (child <= self.xu)
                )
            )

    def test_zero_probability(self):

        child = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=0.0,
            rng=self.rng
        )

        np.testing.assert_array_equal(
            child, self.parent
        )

    def test_full_probability(self):

        child = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            rng=self.rng
        )

        self.assertTrue(
            np.any(child != self.parent)
        )

    def test_parent_unchanged(self):

        original = self.parent.copy()

        child = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            rng=self.rng
        )

        child[0] = 0.0

        np.testing.assert_array_equal(
            self.parent, original
        )

    def test_invalid_bounds(self):

        with self.assertRaises(ValueError):

            polynomial_mutation(
                [0.5],
                xl=1.0,
                xu=0.0
            )

    def test_invalid_probability(self):

        with self.assertRaises(ValueError):

            polynomial_mutation(
                [0.5],
                prob=1.5
            )

    def test_invalid_eta(self):

        with self.assertRaises(ValueError):

            polynomial_mutation(
                [0.5],
                eta=-1
            )

    def test_invalid_shape(self):

        with self.assertRaises(ValueError):

            polynomial_mutation(
                [[0.2, 0.4]]
            )

    def test_reproducibility(self):

        a = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            rng=np.random.default_rng(42)
        )

        b = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=1.0,
            rng=np.random.default_rng(42)
        )

        np.testing.assert_array_equal(a, b)

    def test_boundary_individuals(self):

        for parent in [self.xl, self.xu]:

            for _ in range(100):

                child = polynomial_mutation(
                    parent,
                    xl=self.xl,
                    xu=self.xu,
                    prob=1.0,
                    rng=self.rng
                )

                self.assertTrue(
                    np.all(
                        (child >= self.xl)
                        & (child <= self.xu)
                    )
                )

    def test_default_probability(self):

        a = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            rng=np.random.default_rng(42)
        )

        b = polynomial_mutation(
            self.parent,
            xl=self.xl,
            xu=self.xu,
            prob=1.0 / len(self.parent),
            rng=np.random.default_rng(42)
        )

        np.testing.assert_array_equal(a, b)


if __name__ == "__main__":
    unittest.main()
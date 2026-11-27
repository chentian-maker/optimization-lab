import unittest
import numpy as np

from optimization_lab.algorithms import tournament_selection


class TestSelection(unittest.TestCase):

    def setUp(self):

        self.ranks = np.array([1, 1, 2, 3])

        self.crowding = np.array([
            0.5, 1.5, 2.0, 3.0
        ])

        self.rng = np.random.default_rng(42)

    def test_output_shape(self):

        selected = tournament_selection(
            self.ranks,
            self.crowding,
            100,
            rng=self.rng
        )

        self.assertEqual(selected.shape, (100,))

    def test_valid_indices(self):

        selected = tournament_selection(
            self.ranks,
            self.crowding,
            100,
            rng=self.rng
        )

        self.assertTrue(
            np.all((selected >= 0) & (selected < 4))
        )

    def test_rank_priority(self):

        selected = tournament_selection(
            [1, 2],
            [0.1, 100.0],
            20,
            rng=self.rng
        )

        self.assertTrue(np.all(selected == 0))

    def test_crowding_priority(self):

        selected = tournament_selection(
            [1, 1],
            [0.5, 2.0],
            20,
            rng=self.rng
        )

        self.assertTrue(np.all(selected == 1))

    def test_infinite_crowding(self):

        selected = tournament_selection(
            [1, 1],
            [0.5, np.inf],
            20,
            rng=self.rng
        )

        self.assertTrue(np.all(selected == 1))

    def test_invalid_lengths(self):

        with self.assertRaises(ValueError):

            tournament_selection(
                [1, 2],
                [0.5],
                10
            )

    def test_invalid_population_size(self):

        with self.assertRaises(ValueError):

            tournament_selection(
                [1],
                [0.5],
                10
            )

    def test_reproducibility(self):

        a = tournament_selection(
            self.ranks,
            self.crowding,
            100,
            rng=np.random.default_rng(42)
        )

        b = tournament_selection(
            self.ranks,
            self.crowding,
            100,
            rng=np.random.default_rng(42)
        )

        np.testing.assert_array_equal(a, b)


if __name__ == "__main__":
    unittest.main()
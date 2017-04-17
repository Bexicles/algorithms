import unittest
from quicksort_pivot_median_inplace import run_quicksort


class SortArraysTest_1(unittest.TestCase):
    def test_sorted_arrays(self):

        self.assertEqual([5], run_quicksort([5]))
        self.assertEqual([7, 9], run_quicksort([9, 7]))
        self.assertEqual([1, 2, 6, 7], run_quicksort([6, 7, 2, 1]))
        self.assertEqual([1, 2, 3], run_quicksort([3, 2, 1]))
        self.assertEqual([1, 3, 6, 8, 11], run_quicksort([3, 6, 11, 1, 8]))
        self.assertEqual([1, 3, 5, 6, 8, 10, 11], run_quicksort([5, 3, 6, 11, 1, 8, 10]))





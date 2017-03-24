import unittest
from quicksort_pivot_first import run_quicksort


class SortArraysTest_2(unittest.TestCase):
    def test_number_comparisons(self):
        self.assertEqual(0, run_quicksort([5])[1])
        self.assertEqual(1, run_quicksort([9, 7])[1])
        self.assertEqual(4, run_quicksort([6, 7, 2, 1])[1])
        self.assertEqual(3, run_quicksort([3, 2, 1])[1])
        self.assertEqual(7, run_quicksort([3, 6, 11, 1, 8])[1])
        self.assertEqual(9, run_quicksort([311, 206, 100, 184, 288])[1])


class SortArraysTest_1(unittest.TestCase):
    def test_sorted_arrays(self):

        self.assertEqual([5], run_quicksort([5])[0])
        self.assertEqual([7,9], run_quicksort([9, 7])[0])
        self.assertEqual([1,2,6,7], run_quicksort([6, 7, 2, 1])[0])
        self.assertEqual([1,2,3], run_quicksort([3, 2, 1])[0])
        self.assertEqual([1,3,6,8,11], run_quicksort([3, 6, 11, 1, 8])[0])





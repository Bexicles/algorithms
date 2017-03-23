import unittest
import QuickSort.quickSort_firstPivot as QS

class SortArraysTest(unittest.TestCase):
    def TestQuickSort(self):
        self.assertEqual([5], QS.runQuickSort([5]))
        self.assertEqual([7, 9], QS.runQuickSort([9, 7]))
        self.assertEqual([1, 2, 6, 7], QS.runQuickSort([6, 7, 2, 1]))
        self.assertEqual([1, 2, 3], QS.runQuickSort([3, 2, 1]))
        self.assertEqual([1, 3, 6, 8, 11], QS.runQuickSort([3, 6, 11, 1, 8]))
        self.assertEqual([100, 184, 206, 288, 311], QS.runQuickSort([311, 206, 100, 184, 288]))

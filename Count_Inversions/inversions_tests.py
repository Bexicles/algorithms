import unittest
import inversions as inv




class CountInversionsTests(unittest.TestCase):
    def test_inversion_counter(self):
        self.assertEqual(2, inv.count_inversions([3, 1, 2, 4, 5, 6, 7, 8])[1], "Expected 2 inversions")
        self.assertEqual(2, inv.count_inversions([3, 1, 2])[1], "Expected 2 inversions")
        self.assertEqual(3, inv.count_inversions([3, 1, 2, 4, 5, 6, 7, 8, 10, 9])[1], "Expected 3 inversions")
        self.assertEqual(45, inv.count_inversions([1000, 900, 800, 700, 600, 50, 40, 30, 2, 0.1])[1], "Expected 45 inversions")
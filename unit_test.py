import unittest
from solve import BruteForce, Memoization, DynamicProgramming


class UnitTest(unittest.TestCase):
    def test1(self):
        target = 100
        arr = [32, 24, 56, 7, 8, 9, 20, 34, 53, 23, 92, 54, 76, 85, 70, 43]
        size = len(arr)
        brute = BruteForce(size, target)
        dp = DynamicProgramming(size, target)
        memo = Memoization(size, target)
        self.assertTrue(brute.recursive_function(arr, size, target))
        self.assertTrue(dp.solve(arr, size, target))
        self.assertTrue(memo.solve(arr, size, target))

    def test2(self):
        target = 1000
        arr = [321, 242, 563, 75, 58, 94, 278, 349, 530, 230, 926, 544, 763, 853, 704, 435, 345, 546, 776, 454, 343]
        size = len(arr)
        brute = BruteForce(size, target)
        dp = DynamicProgramming(size, target)
        memo = Memoization(size, target)
        self.assertTrue(brute.recursive_function(arr, size, target))
        self.assertTrue(dp.solve(arr, size, target))
        self.assertTrue(memo.solve(arr, size, target))

    def test3(self):
        target = 9
        arr = [3, 5, 7, 8, 32, 23]
        size = len(arr)
        brute = BruteForce(size, target)
        dp = DynamicProgramming(size, target)
        memo = Memoization(size, target)
        self.assertTrue(brute.recursive_function(arr, size, target))
        self.assertTrue(dp.solve(arr, size, target))
        self.assertTrue(memo.solve(arr, size, target))
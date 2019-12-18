from unittest import TestCase

from .max_profit import Solution

class TestMaxProfit(TestCase):
    def test_with_input_max_profit_exists(self):
        result = Solution().max_profit([7,1,5,3,6,4])
        self.assertEqual(result, 5)

    def test_with_another_input(self):
        result = Solution().max_profit([2, 4, 1])
        self.assertEqual(result, 2)

    def test_with_input_no_max_profit_exists(self):
        result = Solution().max_profit([7,6,4,3,1])
        self.assertEqual(result, 0)

    def test_with_no_input_data(self):
         result = Solution().max_profit([])
         self.assertEqual(result, 0)

    def test_with_non_list_input(self):
         result = Solution().max_profit(1234)
         self.assertEqual(result, 0)

         result = Solution().max_profit("1234")
         self.assertEqual(result, 0)

         result = Solution().max_profit({})
         self.assertEqual(result, 0)
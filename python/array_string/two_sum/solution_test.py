from unittest import TestCase

from .solution import Solution


class TestTwoSum(TestCase):
    def test_list_with_element_that_have_sum(self):
        nums = [0, 2, 4, 6, 7]
        result = Solution().twoSum(nums, 13)
        self.assertListEqual(result, [3, 4])

    def test_list_with_element_that_have_no_sum(self):
        nums = [0, 2, 4, 6, 7]
        result = Solution().twoSum(nums, 20)
        self.assertListEqual(result, [])

    def test_with_invalid_input(self):
        nums = "abcdefgt"
        result = Solution().twoSum(nums, "ball")
        self.assertListEqual(result, [])

    def test_with_list_of_alphanumeric(self):
            nums = [1, 2, 3, 'b', '=']
            result = Solution().twoSum(nums, 2)
            self.assertListEqual(result, [])


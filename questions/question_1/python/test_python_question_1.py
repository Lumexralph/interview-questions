from solution_1 import Solution

class TestAddTwoNumbersSolution:
    def test_digit_set_1(self):
        l1 = Solution().generate_linked_list(112)
        l2 = Solution().generate_linked_list(345)
        result = Solution().addTwoNumbers(l1, l2)

        assert result.val == '7'
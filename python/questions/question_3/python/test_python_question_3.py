from solution_3 import Solution

class TestValidExpressionSolution:
    def test_invalid_expression(self):
        result = Solution().isValid('()(){(())')
        assert result == False

    def test_valid_expression(self):
        result = Solution().isValid('([{}])()')
        assert result == True

    def test_empty_string_expression(self):
        result = Solution().isValid('')
        assert result == True

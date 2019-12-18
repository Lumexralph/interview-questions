from unittest import TestCase

from .urlify import Solution


class TestURLify(TestCase):
    def test_string_with_spaces_is_urlified(self):
        result = Solution().urlify("a b", 3)
        self.assertEqual(result, "a%20b")

    def test_string_with_not_enough_length(self):
        result = Solution().urlify("a c b", 3)
        self.assertEqual(result, "")

    def test_with_invalid_inpu(self):
        result = Solution().urlify([], {})
        self.assertEqual(result, "")
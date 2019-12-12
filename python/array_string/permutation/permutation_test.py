from unittest import TestCase

from .permutation import Solution


class TestCheckPermutation(TestCase):
    def test_strings_same_character_different_order(self):
        result = Solution().check_permutation("abcd", "dcba")
        self.assertTrue(result)

    def test_strings_different_character_different_order(self):
        result = Solution().check_permutation("abcde", "dcba")
        self.assertFalse(result)

    def test_strings_with_different_length(self):
        result = Solution().check_permutation("abcdhgg", "dcbag")
        self.assertFalse(result)

    def test_string_with_same_length_different_characters(self):
        result = Solution().check_permutation("abcdef", "ged cba")
        self.assertFalse(result)

    def test_with_list_and_object(self):
        result = Solution().check_permutation([], {})
        self.assertFalse(result)

    def test_with_empty_strings(self):
        result = Solution().check_permutation("", "")
        self.assertTrue(result)

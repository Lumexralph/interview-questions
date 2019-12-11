from unittest import TestCase

from .is_unique import Solution


class TestIsUnique(TestCase):
    def test_with_unique_characters(self):
        result = Solution().is_unique("abcdefghikjlmnopqrstu")
        self.assertTrue(result)

    def test_with_unique_upper_lowercase(self):
        result = Solution().is_unique("AabcBdefghikjKlmnoMpqrstu")
        self.assertTrue(result)

    def test_with_repeated_upper_lowercase(self):
        result = Solution().is_unique("AAabcBBddefghikjKlmnoMpqqp")
        self.assertFalse(result)

    def test_with_repeated_character(self):
        result = Solution().is_unique("aabccddeeff")
        self.assertFalse(result)

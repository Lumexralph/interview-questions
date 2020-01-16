from unittest import TestCase

from .compression import Solution


class TestStringCompression(TestCase):
    def test_length_of_compressed_and_original_is_same(self):
        result = Solution().compress_str("aabbccdd")
        self.assertEqual(result, "aabbccdd")

    def test_long_string_is_compressed(self):
        result = Solution().compress_str("aaabbbcccdddAA")
        self.assertEqual(result, "a3b3c3d3A2")

    def test_with_empty_string(self):
        result = Solution().compress_str("")
        self.assertEqual(result, "")

    def test_with_non_string(self):
        result = Solution().compress_str([])
        self.assertEqual(result, "")
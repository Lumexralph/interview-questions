# from __future__ import annotations

class Solution:
    def is_unique(self, string: str) -> bool:
        # to achieve a time complexity O(n) and
        # amortized space complexity O(1) - O(logn)

        char_set = {}

        for char in string:
            # if we have already seen this character
            if char_set.get(char):
                return False

            char_set[char] = True

        return True
from collections import defaultdict

class Solution:
    def compress_str(self, word: str) -> str:
        # validations
        if len(word) == 0 or not isinstance(word, str):
            return ""

        compressed_str_list = []
        char_count = defaultdict(int)

        i = 0
        while i < len(word):
            char = word[i]
            char_count[char] += 1
            # look ahead
            i += 1

            try: # we will have an index beyond the word index range
                if word[i] not in char_count:
                    # collate the accumulated result
                    compressed_str_list.append(char + str(char_count[char]))
                     # reset because there's a new char next
                    char_count = defaultdict(int)
            except IndexError:
                # get the last char in the dict
                compressed_str_list.append(char + str(char_count[char]))

        compressed_str = "".join(compressed_str_list)
        print(compressed_str)
        return compressed_str if len(compressed_str) < len(word) else word


print(Solution().compress_str("aaabbbcccdddAAaaCCC"))
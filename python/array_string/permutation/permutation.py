# Assumptions made, there will be repeated characters
# whitespace counts in permutation
# It is case sensitive
class Solution:
    def check_permutation(self, data_A: str, data_B: str) -> bool:
        # validations
        if len(data_A) != len(data_B) or not isinstance(data_A, str) \
            or not isinstance(data_B, str):
            return False

        # key - index, value - character
        data_A_info = {}

        formed_data = list(data_B)

        for i in range(len(data_A)):
            if data_A_info.get(data_A[i]):
                data_A_info[data_A[i]]["count"] += 1
                data_A_info[data_A[i]]["index"].append(i)
            else:
                data_A_info[data_A[i]] = {"count": 1, "index": [i]}

        # arrange data_B like data_A
        for char in data_B:
            if data_A_info.get(char):
                index = data_A_info[char]["index"][0]

                formed_data[index] = char

                # we need to remove the used index incase of
                # repeated characters
                del data_A_info[char]["index"][0]
                data_A_info[char]["count"] -= 1

                if data_A_info[char]["count"] == 0:
                    del data_A_info[char]

        return "".join(formed_data) == data_A


print(Solution().check_permutation("aAbgcdeg", "edcbagg"))

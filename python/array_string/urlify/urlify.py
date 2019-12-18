# This implementation assumes that every spaces
# will be replaced with %20
from ctypes import py_object


class Solution:
    def urlify(self, string: str, length: int) -> str:
        # validation
        if not string or (len(string) > length) \
            or not isinstance(string, str) or \
            not isinstance(length, int):
            return ""

        # we need array the capacity of the length
        urlify_string = (length * py_object)()
        start = 0
        end = length - 1

        while start <= end:
            if string[start] == " ":
                urlify_string[start] = "%20"
            else:
                urlify_string[start] = string[start]

            if string[end] == " ":
                urlify_string[end] = "%20"
            else:
                urlify_string[end] = string[end]


            start += 1
            end -= 1

        return "".join(urlify_string)


print(Solution().urlify("a b", 3))
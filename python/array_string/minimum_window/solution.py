from __future__ import annotations
from collections import Counter


def min_window(s: str, t: str) -> str:
    # validation
    if len(s) == 0 or len(t) == 0 \
        or not isinstance(s, str) \
        or not isinstance(t, str) \
        or len(t) > len(s):
        return ""

    # desired character
    desired = Counter(t)

    # create a dictionary to keep tracks of char in t
    t_char = {}

    # populate the t_char
    for char in t:
        t_char[char] = 0

    # keep track of the missing character in s from t
    missing_count = len(t_char)
    shortest_range = [float('-inf'), float('inf')]

    slow_index, fast_index = 0, 0

    while fast_index < len(s):
        # if we find part of the character we're looking for
        if t_char.get(s[fast_index]) is not None:
            # increment the match
            t_char[s[fast_index]] += 1

            # check value was not tracked and is same count as desired
            if t_char[s[fast_index]] == desired[s[fast_index]]:
                missing_count -= 1

        # when the missing_char count is 0, that means
        # we are in the window that contains all the characters in t
        # update the shortest range
        while missing_count == 0:
            # update the shortest range
            if (fast_index - slow_index) < (shortest_range[1] - shortest_range[0]):
                shortest_range[0] = slow_index
                shortest_range[1] = fast_index

            # if we find part of the character we're looking for
            if t_char.get(s[slow_index]) is not None:
                # decrement the occurrence to indicate a match
                # in the current window
                t_char[s[slow_index]] -= 1

                # if the value 0 means it is missing
                if t_char[s[slow_index]] < desired[s[slow_index]]:
                    missing_count += 1

            # keep shrinking the matching window
            slow_index += 1

        # move the fast pointer
        fast_index += 1

    # return the shortest window
    return "" if shortest_range[0] == float('-inf') else s[shortest_range[0] : shortest_range[1] + 1]

S = "ADOBECODEBANC"
T = "ABC"
print(min_window(S, T))

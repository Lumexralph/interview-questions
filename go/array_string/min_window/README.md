# Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## Algorithm

1. We start with two pointers, left and right initially pointing to the first element of the string SS.

2. We use the right pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of TT.

3. Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.

4. If the window is not desirable any more, we repeat step \; 2step2 onwards.

## Algorithm Complexity

* Time Complexity - O(n)
* space Complexity - Amortized O(1)

[Further Reading](https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66)

## Run tests

    go test solution_test.go
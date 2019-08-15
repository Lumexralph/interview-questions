"""Module containing the solution to the question"""
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep track of open brackets
        stack = deque()

        mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # moving through every character in the string
        for char in s:

            # if the charcater is a closing bracket
            if char in mapping:

                # pop the topmost element from the stack, if it is not empty, otherwise assign a dummy value
                temp_char = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != temp_char:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

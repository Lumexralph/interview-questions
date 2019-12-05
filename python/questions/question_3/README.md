# Question/Problem Statement

 Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.


        Input: "((()))"
        Output: True

        Input: "[()]{}"
        Output: True

        Input: "({[)]"
        Output: False

## Algorithmic  / Asymptotic Analysis 

I struggled a bit with this question but got a solution that inspired me on https://leetcode.com

Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1)O(1) time.

Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.

Though we are using a hash-map. So space complexity takes a hit.

### Python Solution




### Go Solution


### Rust Solution


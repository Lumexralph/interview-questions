# Sum Two Reversed Linked Lists

 You are given two linked-lists representing two
 non-negative integers. The digits are stored in reverse
 order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

## Algorthmic  / Asymptotic Analysis

The main operation which is `generate_linked_list` and `addTwoNumbers` all have assignment operations which occurs at constant time O(1) but the significant difference would be in the `while` and `for` loop.

In `retrive_values` function, the loop will run operations as the size of the linked_list increases - linear time `O(n)`, same can be said of `generate_linked_list` method which uses the length of the number string supplied i.e

    n + n + 1 = 2n + 1

What is significant is n, hence the algorithm is `O(n)`

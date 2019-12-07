# Question/Problem Statement

 Given a string, find the length of the longest substring without repeating characters.

    Input: 'abrkaabcdefghijjxxx'
    Output: 10


## Algorthmic  / Asymptotic Analysis [WIP]

The growth rate of the running time as a function of the input size n,

### Python Solution

The operations of assigning values and initializing variables `initial_length, current_length`, the swap and branch of
`if current_length > initial_length:`, `Solution.records.get(char)` happens in constant time `O(1)` but a loop was needed to go through
the characters in the string and the loop will run or perform operations as the size of the string grows, hence a linear time `O(n)`

The algorithm will run in -  O(n)

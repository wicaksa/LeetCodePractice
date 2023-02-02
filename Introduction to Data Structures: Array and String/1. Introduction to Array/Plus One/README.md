# Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Exmples

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

## Constraints

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

## Approach

I wanted to do this problem in place so I started iterating from the end of the array
working my way towards the front. I had a counter in place to keep track of whether
or not I will need to carry over a 1. If the value at the current index becomes a 10,
that's when I would need to keep track of the one but also need to change that value
to a 0. In the case that the pointer goes out of bounds, meaning the input was some
variation of 999, I will need to add a leading 1. Nums is returned at the end.

## Time and Space Complexities

Time: O(N) - One pass through the array at worst case.
Space: O(1) - Did not need to use extra space. Modified array in place.

# Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

## Examples

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

## Constraints

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

## Approach

This problem was fairly straight forward. I used two pointers starting at the ends of the array. Once the values were swapped, I moved the pointers toward the center. When both pointers crossed one another, that's the cue to stop iteration.

## Review and Evaluate

### Time Complexity

This problem has a worst case scenario O(N).

### Space Complexity

This problem has a space complexity of O(1) since we did not initialize any additional data structures to store the result.

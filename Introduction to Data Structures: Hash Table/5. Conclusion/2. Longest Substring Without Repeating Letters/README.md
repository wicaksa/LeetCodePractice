# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

## Examples

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Constraints

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

## Approach
1. I used a hash set to keep track of seen elements. This solution also requires the use of two pointers. The leading pointer will check if the character is already in the set. If it is not, we add the character to the set, update the max value, then increment pointer. If it is, we remove the element in the set that the behind pointer is at then increment that pointer. We do this until the leading pointer goes out of bounds. Then we can return the max value. 

## Review & Evaluate
1. Time Complexity: O(M+N) since we are iterating two pointers. Space:O(N) since we are using one hash map.

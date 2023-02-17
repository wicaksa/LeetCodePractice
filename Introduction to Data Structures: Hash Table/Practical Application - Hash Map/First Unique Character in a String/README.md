# First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## Examples 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

## Constraints

    1 <= s.length <= 105
    s consists of only lowercase English letters.

## Approach
I used a hash map to implement the solution. First, I iterated through the input and save each char as a key and the count of each char as a value. Then, I loop through each key and see if the value is 1. If it is, we just return the index of where that element was found in the original string. 

## Review & Evaluate
- Time Complexity: O(M+N). We have two iterations: the string then the list of keys which may have different lengths.
- Space Complexity: O(N). We used one hash map to store elements.
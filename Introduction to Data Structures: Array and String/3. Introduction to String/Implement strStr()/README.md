# Implement strStr()

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Examples

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

## Constraints

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

## Approach

Before doing the problem, i checked for possible edge cases. There were 3 that I could think of. They are if the length of haystack is 0, the length of needle is 0, and the length of needle is greater than length of haystack. In any of these cases, I would return a -1 since it would be impossible to find needle in haystack.

Next, I found the length of needle. I used this number as the size of my window to slide through haystack.

After that was calculated, it was time to check haystack for any instances of needle. I started iterating at index 0 until index of the length of haystack minus the window plus 1 since the end exclusive.

During the iterations, if at any point it found matching substring in haystack, the algorithm would return the current index, which is the beggining index of the sliding window.

If the for loop exits, it means that there were no instances of needle in a haystack. Therefore, we just return a -1.

## Review and Evaluate

Time Complexity: The upper bound for this algorithm is O(N) since we will be iterating through haystack.

Space complexity: Since we did not create an extra space to store our result, the space complexity is just O(1).

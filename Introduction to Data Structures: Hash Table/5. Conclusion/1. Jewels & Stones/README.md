# Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

## Examples

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

## Constraints

    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.

## Approach
1. I used a hash map to solve this problem. First, I created a hash map to store all of the elements in the first list as a key with values 0. Then, I iterated through the second list. At each iteration, I check whether or not the key is present in the hash map. If it is, we add a 1 to the value. At the end, we just return the sum of the values. 

## Review & Evaluate
1. Time Complexity: O(M+N) since we are iterating both input arrays. Space: O(M).
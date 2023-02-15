# Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Examples

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

## Constraints

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

## Approach
I solved this problem by using a hash map. I iterated through the indices of each string. At each iteration, I check if the element in string s is a key value in the hash map. If it is not, we need to check if the element in string t is a value. If it is not, can add the key value pair. Else, we return false since we cannot have two different keys mapping to the same value. 
If the element at string s is a key of the hash map, we check if the value of that key equals the element in string t. If they differ, we can again return false. If the loop exits, that means all of the letters have the correct mapping so we can return true. 

## Review & Evaluate

### Time and Space Complexities
- Time complexity is O(N) since we are iterating through the inputs of the same length. Operations regarding the dictionaries are all at constant time so no need to add that to the calculation.
- Space complexity is O(N) since we are using an additional space by initializing a hash map. 
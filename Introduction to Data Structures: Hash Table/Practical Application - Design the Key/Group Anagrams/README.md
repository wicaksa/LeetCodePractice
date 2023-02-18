# Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

## Constraints

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

## Approach
1. My first approach involves converting the string to a list, sorting the list, then joining it back to a string. This serves as my key. From here, I check if the hash map contains this key. If it does not, I create a new list with the original string and insert it as a value for that key. If it does, I simply append the original string to the value. 
2. This approach is similar to the first one but instead of sorting the list as a key, I used a list to keep track of how many of each letter was present in the word then using that as a key.

## Review and Evaluate
1. Time : (M * N log N), Space = O(N+M)
2. Time : (M * N), M length of input, N is average length of each word. Space = O(N) since we are using hash map.
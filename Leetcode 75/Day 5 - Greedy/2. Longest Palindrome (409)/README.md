# Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

## Examples

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

## Constraints

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

## Approach
1. When talking about a palindrome, we have two types. One odd and one even. Even palindromes are easy to make. You just have even numbers of all your letters and put them on each side. For odd palindromes, it's the same thing but you have an odd number of letters in the middle. So when doing this algorithm, you will add up all of the letters that are even. If there is an odd number, you simply subtract 1 to form an even number. Then at the end, you simply add 1 to represent putting any of the odd count letters in the middle of the palindrome. 

## Review & Evaluate
1. Time: O(N) Space: O(N)

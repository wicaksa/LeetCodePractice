# Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Examples

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = " hello world "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

## Constraints

- 1 <= s.length <= 104
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

### Follow-up

If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

## Approach

My first approach was using one pointer. I iterate from the end of the string towards the beggining. At each iteration, I check whether or not the character is a letter or is a space. If it is a letter, I will append it to a temporary string. If it's a space, I append the temporary string to the result and clear the result only if the temporary string is not empty.

## Complexities

### Time Complexity

O(N) since we are doing this problem linearly with one for loop.

### Space Complexity

O(N) since we are using an extra string to hold the result.

# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

## Example

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Constraints=

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

## Approach

### Approach 1

My initial thought into doing this problem came naturally but it may not be the most efficient solution. First, I saw that I will need to check all of the letters of every word in the input list. However, the maximum length of the matching prefix (if there are any) will be of the shortest word in the list. To make this easier, I went ahead and sorted the input. That way, the first word in the list will be the shortest and will be the first for loop that we traverse.

As we check each letter of the first word, we check each letter of each word in the list. If the second iteration passes without fail, meaning that we have found a match in every index that we are looping through, we will append that letter into a resultant string. If at anytime the letter at the current index do not match, we simply return the resultant array.

As for edge cases, we will return an empty string "" if the input array has a length of 0, and we will return the first element of the list if the input array has a length of 1.

## Review & Evaluate

### Time Complexity

- O(N log N) for the sort(). Python uses something called Timsort.
- O(N) for the first for loop.
- O(N) for the second for loop.
- Total = NlogN \* N^2

### Space Complexity

- Total = O(N) since we are using an extra string to store the result.

## Update

At first, i used an extra array to store the result. However, I realized that the result will just be a substring of the first element. So instead, I created a counter to count the number of matching letters. Then I can just return the substring of the first letter from [0:counter]. This will make the space complexity 0(1) making the program run a little faster.

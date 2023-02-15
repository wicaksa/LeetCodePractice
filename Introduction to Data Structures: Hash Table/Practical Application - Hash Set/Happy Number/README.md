# Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

## Examples

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

## Constraints:

    1 <= n <= 231 - 1

## Approach
### Approach 1
For my first approach, I solved this problem using a set to keep track of the numbers that I've seen. I use a while loop to see if the current number is in the set. Inside the while loop, I created a total variable to keep track of the current sum of the squared of the current number's digits. I converted each int to a string in order to easily iterate through the digits. After the loop exits, it checks whether or not 1 is in the set. If it is, we return true. Else we return false. 

## Review & Evaluate
### Space and Time Complexity for Approach 1
- Space: O(N) since we created a set to keep track of the numbers that we've seen. 
- Time: O(N) since at worst, we'll iterate N + 1 time in the while loop to see a number in the set. 
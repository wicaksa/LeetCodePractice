# Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

## Examples

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

## Constraints

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Approach

In this problem, I simply iterated through the list. I kept track of the current number of consecutive ones and the maximum number of consecutive ones. Everytime the pointer lands on a 1, we add 1 to the current number. However, once it reaches 0, we will compare the value from the current and the max and replace the max value if needed.

## Review & Evaluate

### Time Complexity

The time complexity for this problem is just O(N) since we are iterating this list in one pass.

### Space Complexity

The space complexity for this problem is just O(1) since we did not create an extra data structure to store the result.

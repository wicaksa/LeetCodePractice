# Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

## Example

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

## Constraints

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

## Approach

### Approach 1 : Using 2 pointers

My first approach at this problem is using two pointers, a left and a right pointer. With this algorithm, the right pointer will continue moving right until the value becomes >= the target. At this point, we want to store the sub array length then compare that with the current minimum subarray length and replace the value if it's smaller.

Once the right pointer reaches the end, the left pointer moves right until the sum becomes smaller than the target or until the left pointer goes out of bounds.

This solution only passed 18/20 test cases.

### Approach 2: Using two pointers but with a for loop for the right pointer

This solution was built off the first solution. Instead of using two pointers manually, we use a for loop for the right pointer. In addition, we keep a running sum of the array in order to make the program run faster since it's not calculating the sum of the subarray each time we move our pointers.

Essentially, we iterate the for loop pointer until the running sum is greater than or equal to target. When we reach this condition, we will move our left pointer one by one to see if we can find a smaller subarray that still has a sum that is greater than or equal to the target value.

## Review & Evaluate

### Time Complexity

The time complexity for the second approach is O(N) since we have one for loop despite having an inner while loop because the inner while loop will also be moving at worse the length of the array.

### Space Complexity

The space complexity is just O(1) since we did not allocate a new data structure to store the result but just a variable.

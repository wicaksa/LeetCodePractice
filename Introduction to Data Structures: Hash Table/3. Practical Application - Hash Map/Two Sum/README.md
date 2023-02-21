# Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Examples

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

## Constraints

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

## Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Approach
For this problem, I implemented a HashMap. First, we need to iterate through the given input. At each iteration, we check if the difference between the target and the current element exists as a key. If it is not, we need to store the key value pair in the HashMap: the element will be the key and the index will be the value. However, if the element exists as a key, we simply return an integer array containing the current index and the value of the difference. 

## Review & Evaluate

### Time and Space Complexities
- The time complexity for this problem is O(N) since we are looping through the input.
- The space complexity is O(N) since we are using a HashMap to store our data. 
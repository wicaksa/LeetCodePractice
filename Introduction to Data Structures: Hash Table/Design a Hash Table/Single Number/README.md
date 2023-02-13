# Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Example

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

## Constraints 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

## Approach
I used a dictionary to solve this problem. I first iterated through the input and put each element as the key in the dictionary. The value is the amount of times we've seen the number. After iteration is complete, we will iterate through the keys of the dictionary. If any of the values is 1, we will simply return that key.

## Review & Evaluate
### Time Complexity 
O(N) since we iterate through the the input and the keys of the dictionary. This is 2 * O(N) or simply O(N).

### Space Complexity
O(N) since we used a dictionary to solve this problem, the space complexity is going to be O(N) due to the number of elements we will be inserting.
# Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

## Example

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

## Constraints

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105

## Approach
1. I used a hash map in this approach along with iteration of the input. At each iteration, we check if that element is a key in the hashmap. If it's a key and the difference between the current index and the index stored is less than or equal to k, we return true. If not, we update the value of the key to the current index. 

## Review Evaluate 

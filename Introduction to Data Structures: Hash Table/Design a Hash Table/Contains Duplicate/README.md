# Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
## Examples
Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

## Constraints 
Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

## Approach
For this problem, I used a dictionary to solve the problem. I would iterate each element in the input. I would see if there exists that key in the dictionary. If there isn't, I would add that key to the dictionary and increment the value seen to 1. If we already have that key in the dicitonary, we would increment the value seen by 1 then check if the value is greater than 1. If it is, we return a true. If this loop ends without returning true, we will return false. 

## Review and Evaluate
### Time Complexity
The time complexity is just O(N) since we are iterating through each element in the input. The lookup and adding to a dictionary is just an O(1) operataion.

### Space Complexity
The space complexity is O(N) since we are using a dictionary to keep track of which values we have seen. 
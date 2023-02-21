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

## Approach 1
For this problem, I used a dictionary to solve the problem. I would iterate each element in the input. I would see if there exists that key in the dictionary. If there isn't, I would add that key to the dictionary and increment the value seen to 1. If we already have that key in the dicitonary, we would increment the value seen by 1 then check if the value is greater than 1. If it is, we return a true. If this loop ends without returning true, we will return false. 

## Approach 2
For this approach I used a HashSet. I iterate through the input array then check whether or not the element is in the set. If it is, we return true. If it's not, we simply add it to the array and keep iterating. If the loop exits without finding a duplicate, we simply return false. 

## Review and Evaluate

### Time and Space Complexity 1
- The time complexity is just O(N) since we are iterating through each element in the input. The lookup and adding to a dictionary is just an O(1) operataion.
- The space complexity is O(N) since we are using a dictionary to keep track of which values we have seen. 

### Time and Space Complexity 2
- The time complexity is still O(N) since we have to iterate through all of the elements in the input. Lookup time and add time in a HashSet is about O(1).
- The space complexity is O(N) since we are creating a set to store potentially N items. 

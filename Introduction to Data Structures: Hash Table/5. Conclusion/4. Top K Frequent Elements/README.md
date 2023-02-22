# Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Example

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

## Constraints

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Approach
1. This approach involves utilizing a hash map, and an array. First, we needed to create a hash map with the element in the input as the key and how many times they appeared as the value. After this, we move on to the next step. Since the value of k cannot exceed the length of the input array, we can use that length to create another array in order to perform a bucket sort on our hash map. Essentially, we are using the index of this new array as the key which represents the number of times a particular number has appeared. The elements stored at each index will be the number that has appeared that many times. We keep this number stored in an array since there may be more than one number that appeared the same amount of times. After placing each element in our hash map into the new array, we can then iterate from end to beggining of the new array. At each iteration, we check whether or not that index is empty. If it is, we keep on moving. If it's not, we take a look at that element, and append it or them onto our output array. After each append, we check to see if the output array length is equal to k. If it is, we can stop iterating and return the output array.

# Review & Evaluate
1. Time: O(N) Space: O(N)

## Review & Evaluate
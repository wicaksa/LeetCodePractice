# Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Examples

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

## Constraints

- 1 <= nums.length <= 105
- -231 <= nums[i] <= 231 - 1
- 0 <= k <= 105

## Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

## Approach 1: Using pop() and insert()

My initial approach was to pop the last element and insert it in the beginning of the array. We do this as many times as we have k. However when K value gets large, this will take a lot of time to do. So next, I noticed that if the k value is the same size as the array, you essentially will have the same array at the end of the rotation. Hence, any multiple of the length of the array will result in the same thing. So before I did the algorithm, I used modulo division to divide the k value by the length of the array to get a remainder. This remainder will always be less than the length of the array so at most we will rotate it N-1 times.

## Approach 2: Using List Reversal

This approach looks at this algorithm at a quicker time complexity with using constant space. When you look at the first example (where the Input: nums = [1,2,3,4,5,6,7], k = 3 and Output: [5,6,7,1,2,3,4]) you can see that you take the last k number of elements from the end of the list, put them in the front then take the remaining elements and put them in the back. If you were to reverse the list first, you would get [7,6,5,4,3,2,1]. Now you can see that the first 3 elements are in the correct order but need to be reversed and the last 4 elements are in the correct order but need to be reversed.

In this approach you will have to implement your own reverse algorithm or use built in functions supported by your language of choice.

## Review & Evaluate

### Time Compexity

- Approach 1: The time complexity for this problem is O(N^2) due to the fact that we have a for loop and within it we have an insert operation.
- Approach 2: Since Reversing a list takes O(N) time, that gives us a total time complexity of 3 \* O(N).

### Space Complexity

- Approach 1: We used no extra space so the complexity is just O(1).
- Approach 2: We used no extra space similar to the first approach so it is just O(1).

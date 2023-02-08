# Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Examples

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

## Constraints:

- 2 <= numbers.length <= 3 \* 104
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

## Approaches

### Approach 1: Two For Loops

My first approach involved two for loops. The first for loop was used to iterate through the list. The second for loop was used to look for the difference between the target and first element values. This however, ran too slow when input sizes were larget hence it only passed 18/22 test cases.

### Approach 2: One For Loop and One Binary Search

My second approach was built upon the first approach. Instead of using a second for loop, I used a binary search algorithm in order to find the second value.

### Approach 3: Two pointer

My last approach used two pointers, a left and a right. We iterate the pointers until they cross one another. At each iteration, we check if the sum of elements at the two pointers is either greater than, less than, or equal to the target. If they equal, we just return the left pointer + 1 and the right pointer + 1. However, if they are greater than, we will decrement the right pointer. If they are less than, we increment the left pointer. We do this until the answer is found.

## Review and Evaluate

### Time Complexities

- First Approach: O(N2) : Very Slow since we are using nested for loops.
- Second Approach: O(N \* log N) : A bit faster since we incorporated a binary search.
- Third Approach: O(N) : Much faster since this algorithm is linear using two pointers.

### Space Complexities

- All are O(1) since we did not initialize another data structure to store our result.

# Largest Number At Least Twice of Others

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

## Examples

### Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

### Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

## Approach

I first found the max value of the list. Since it's unique, there will only be one instance. Next, I iterate the list. At each iteration, I check whether twice the current value is greater than the max value. If this is true at any point, i will return a -1.

## Complexities

Space: O(1)
Time: O(2N) = O(N)

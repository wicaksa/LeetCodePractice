# Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

## Approach:

First, I calculated the total sum of the array. Then, I iterated through the array while keeping track of the sum of values to the left of the current index. Now at each index, I checked whether the sum of values to the left of the current index equals the sum of the values to the right. To calculate the sum of values to the right of the current index, I used the formula total sum of the array - the sum to the left of the current index - the value of the element at the current index. If at any point this check is true, it will return the current index.

## Review & Evaluate

### Complexities:

Time: O(N) because this algorithm is linear.
Space: O(1) because no extra space is needed.

# Array Partition I

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

## Example

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
   So the maximum possible sum is 4.

Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 +

## Approach

At first glance, my initial thought was either implementing a dictionary or finding out all the possible pairs then calculating the result that way. But after some more understanding, I saw that if I sorted the list, the resultant list is what the best possible pairing should be. So in order to get minimum value, I just travesersed the sorted list by every other index starting from 0 and added that to the total sum variable then return it.

## Review & Evaluate

### Time Complexity:

- Since we are sorting, the worst case scenario is N log N.
- In addition, we have a for loop where we are iterating which is O(N).
- All together, the time complexity is N log N \* N.

### Space complexity

- Since we did not allocate a new list/array, the time complexity is just O(1) for the variable we created to store the answer.

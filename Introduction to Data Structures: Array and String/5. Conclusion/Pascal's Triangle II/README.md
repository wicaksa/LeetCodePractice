# Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

## Examples

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

## Constraints

- 0 <= rowIndex <= 33

## Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

## Approach

- Approach1: This approach was just implementing the Pascal's Triangle algorithm and returning the last element in the resultant array.

## Review and Evaluate

### Time Complexity

- Approach1: The time complexity is just O(N^1) due to our double for loop.

### Space Complexity

- Approach1: the space complexity is O(N^2) since we're storing the result in the array of size n^2.s

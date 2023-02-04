# Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.Example 1:

## Examples

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## Approach:

At first glance, this problem seemed easy to do. My initial thought was to traverse the top row, the right edge, the bottom edge, and then the left edge. In between those steps, you have to remember that you need to not traverse through those rows and columns again. Otherwise, you would be going in an infinite circle. To combat this, I created minimum and maximum values for both row and column. These served as my boundaries. Once you have traversed an edge, you would either increase or decrease the values in order to push the boundaries inward.

When I was implementing this program however, I had trouble with some test cases. After finishing the traversal, it would always add an extra number so my answer was always one element bigger than the result. I realized that the issue was within my while loops. I just needed to add checks before I did the operations in order to prevent it from happening.

## Complexities

Time: O(N): The amount of total elements in the result is the same as the total number of elements in the input (mxn).
Space: O(N): We created an extra array in order to store our result.

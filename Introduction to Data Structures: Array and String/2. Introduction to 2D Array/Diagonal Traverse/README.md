# Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

## Example

Example 1:

Input: mat = [ [1,2,3],[4,5,6],[7,8,9] ]

Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

## Approach

This problem was difficult for me to approach. But after some thinking, I noticed that there are only a few directions that you can take when you're at a specific element. That is, you can either go up + right, right, down + left, down.

In order to figure out when to move in a particular direction, you have to see that at the element where the sum of the coordinates, that is x + y, are even, you want to go up then right or right. When the sum of the coordinates are odd, you want to only go down then left or down. You would repeat this process until you have all numbers in the matrix accounted for.

You also have to watch out for an edge case where the initial matrix is of size 0. In that instance, you would want to return an empty array.

## Complexities

- Time : O(N) since we are iterating as many times as the total number number of elements in the array.
- Space: O(N) since we have to allocate an extra array to store the result.

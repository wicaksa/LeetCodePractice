# Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

## Examples

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

## Approach

I was not sure how to approach this problem. I first started writing psuedo code in order to see if i can get the right number of output. After that was done, I started to look for patterns. I saw that the first and last elements of the resultant sub array is always a one. However, the numbers in the middle were the ones that needed to have it be the sum of the numbers above. I also noticed that when you're in the current index, say for example index 1, the two numbers above have an index of 1 and one. After converting that to a variable, it was just simply i and i-1. Once I figured this out, writing the rest of the code was easy.

First, you need to initialize an empty array in order to store the result. Next, you will have to iterate from 0 to numsRow. This is because you will have to 5 elements in your main result array. After this, you will need to initialize another empty array that will go inside the main result array. To populate this array, you will need to iterate again, since you see that at each result index, you have increasing corresponding array sizes. Next comes the main logic. If the current index that you're iterating is either a 0 or the last index, the result will be a 1. If not, you will need to add the the two values above the current index. After this, you will append the result to the temporary array. After this inner loop runs, you can append it to the main result array.

## Complexities

Time: O(N^2) because we have 2 for loops within one another.
Space: O(N^2) because we have 2 arrays: one to store the result and one temporary array.

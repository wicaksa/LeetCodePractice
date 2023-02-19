# Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

## Approach
1. My first approach involved using a set. I checked each row, column, and 3x3 grid to see if we have seen the element in the set. If we did, we return False. Otherwise, we return true after the loop ends.

2. My second approach involved using a hash set. For the rows and columns, the key is the row and column number itself. For the grid, I used a coordinate where the x is the row // 3 and the y is the col // 3. At each element, I check each hash set to see if we have that number stored. If we have, we simply return false. But if we haven't, we are going to add that element to each of the sets. This loop will run and check every element in the 9x9 grid. If it exits, that means the sodoku board is valid so we return true. 

## Review and Evaluate 
1. Time: 3 * O(81) since we are looping through row, col, and grid 3x. Space: O(81).

2. Time: O(81) since we are looping through the grid once. Space(3 * O(81)).
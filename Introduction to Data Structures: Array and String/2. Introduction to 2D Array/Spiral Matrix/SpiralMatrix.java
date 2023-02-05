class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        // initialize an empty ArrayList to store the result
        List <Integer> result = new ArrayList(); 
        
        // edge case: occurs when the length of input is 0
        if (matrix.length == 0) {
            return result;
        }
        
        // create variables to represent left, right, top, and bottom boundaries
        int leftCol = 0;
        int rightCol = matrix[0].length - 1; 
        int topRow = 0;
        int bottomRow = matrix.length - 1;
        
        // while the left boundary is less than or equal to the right boundary
        // while the top boundary is less than or equal to the bottom boundary
        while (leftCol <= rightCol && topRow <= bottomRow) {
        
            // move to the right
            for (int col = leftCol; col <= rightCol; col++) {
            
                // add element to result
                result.add(matrix[topRow][col]);
            }
            
            // remove top boundary from calculation
            topRow++;
            
            // move down
            for (int row = topRow; row <= bottomRow; row++) {
        
                // add element to result
                result.add(matrix[row][rightCol]);
            }
            // remove right boundary from calculation
            rightCol--; 
            
            // check if the top row <= the bottom row 
            if (topRow <= bottomRow) {
        
                // if it is go left
                for (int col = rightCol; col >= leftCol; col--) {
        
                    // add element to result
                    result.add(matrix[bottomRow][col]);
                }
            }
            
            // remove bottom boundary from calculation
            bottomRow--;
            
            // check if the left boundary <= right boundary
            if (leftCol <= rightCol) {
        
                // if it is go up
                for (int row = bottomRow; row >= topRow; row--) {
        
                    // add element to result
                    result.add(matrix[row][leftCol]);  
                }    
            }
            // remove left boundary from calculation
            leftCol++;
        }
        // return result
        return result;
    }
}
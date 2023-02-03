class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
       
        // input : matrix 
        // output: int [] arr
        
        // edge case when mat size is 0 
        if (mat.length == 0) {
            return new int [0];
        }
        
        // initialize variables: x and y coord, # times we need to iterate, result
        int x = 0;
        int y = 0;
        int l = mat.length * mat[0].length;
        int [] result = new int [l]; 
        
        // while number of times we need to iterate > 0 
        for (int i = 0; i < l; i++) {
        
            // append current matrix at [x][y] to the result array
            result[i] = mat[x][y];
        
            // case1: if x + y is even
            if ( (x + y) % 2 == 0 ) {
        
                // case: if you can go up and right
                if ( (x - 1) >= 0 && (y + 1) < mat[0].length ) {
                    x--; // go up
                    y++; // go right
                }
        
                // case: if you can't go up but can go right
                else if ( (x - 1) < 0 && (y + 1) < mat[0].length) {
                    y++; // go right
                }
        
                // case: if you can't do any of the above, go down 
                else {
                    x++; // go down
                }
            }
            // case2: if x + y is odd
            else {
        
                // case: if you can go down and left
                if ( (x + 1) < mat.length && (y - 1) >= 0 ) {
                    x++; // go down
                    y--; // go left
                }
        
                // case: if you can go down but not left
                else if ( (x + 1) < mat.length && (y - 1) < 0 ) {
                    x++; // go down
                }
        
                // case: if can't do any of the above, go right
                else {
                    y++; // go right
                }
            }
        }
        // return result
        return result;
        
    }
}
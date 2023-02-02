class Solution {
    public int[] plusOne(int[] digits) {
        
        // edge case if length of input is 0
        if (digits.length == 0) {
            return digits;
        }
        
        // create a pointer to go right -> left
        int pointer = digits.length - 1;
        
        // create a counter to keep track of the 1's we need to carry
        int carry = 1;
        
        // while you have a 1 to carry and pointer > -1
        while (carry == 1 && pointer > -1) {
        
            // add one to the current element
            digits[pointer]++;
        
            // decrement the carry
            carry--;
        
            // if that element becomes a 10
            if (digits[pointer] == 10) {
        
                // change it to a 0
                digits[pointer] = 0;
        
                // increment the carry 
                carry++;
        
                // decrement the pointer 
                pointer--;
            }
        }
        // if the carry is not 0 (digits is some variation of [0,0,0,0,0])
        if (carry != 0) {
            // create a new array of an extra size
            digits = new int [1 + digits.length];

            // add 1 to the beggining of the array
            digits[0] = 1;
        }
        
        // return input array
        return digits;
        
                
    }
}
class Solution {
    public String reverseWords(String s) {
        
        // Clean up the string and remove leading and trailing spaces
        s = s.strip();
        
        // Initialize String result and temp to store answer and temporary word
        String result = "";
        String temp = "";
        
        // Iterate from right to left
        for (int i = (s.length() - 1); i >= 0; i--) {
            
            // If char at index i is not a white space
            if (s.charAt(i) != ' ') {
                
                // Append the char to the temporary String
                temp = s.charAt(i) + temp;
            }
            
            // If char at index i is a white space
            else {
                
                // If the temporary String is not empty
                if (temp.length() != 0) {
                    
                    // Append the temporary String to the result String
                    result = result + temp + " ";
                    
                    // Reset the temporary String
                    temp = "";
                }
            }
        }
        
        // You will have something in the temporary String when you finish iterating
        // Append the remaining String here
        return result + temp; 
    }
}
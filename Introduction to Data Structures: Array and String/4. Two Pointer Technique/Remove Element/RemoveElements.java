public class Solution {
    public int removeElement(int[] nums, int val) {
        // two pointer approach, swap values 
        
        // edge case : length of array = 0
        int l = nums.length;
        
        if (l == 0) {
            return l;
        }
        
        // create pointers, counter, temp variables
        int counter = 0;
        int kf = l - 1; // k finder 
        int t  = l - 1; // trailing 
        int temp;
        
        // while kf >= 0
        while (kf >= 0) {
        
            // if nums[kf] != val
            if (nums[kf] != val) {
                // decrement kf
                kf--;
            }
            // else
            else {
                // swap 
                temp = nums[t];
                nums[t] = nums[kf];
                nums[kf] = temp;
                
                // decrement pointers
                kf--;
                t--;
        
                // increment counter
                counter++;
            }
        }
        // return length of array - counter
        return l - counter;
    }
} {
    
}

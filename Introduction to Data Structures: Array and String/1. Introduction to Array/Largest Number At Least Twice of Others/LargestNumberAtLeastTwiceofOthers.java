class Solution {
    public int dominantIndex(int[] nums) {
        
        // edge case: length = 0 or 1 
        if (nums.length == 0) {
            return -1;
        }
        
        if (nums.length == 1) {
            return 0;
        }
        
        // find the largest value in the list and it's index
        int maxVal = -1;
        int indexMax = -1;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > maxVal) {
                maxVal = nums[i];
                indexMax = i;
            }
        }
        
        // iterate through the array
        for (int i = 0; i < nums.length; i++) {
        
            // if 2 * current value > max value and is not max val
            if (2 * nums[i] > maxVal && i != indexMax) {
        
                // return -1
                return -1;
            }
        }
        // return index of max value
        return indexMax;
    }
}
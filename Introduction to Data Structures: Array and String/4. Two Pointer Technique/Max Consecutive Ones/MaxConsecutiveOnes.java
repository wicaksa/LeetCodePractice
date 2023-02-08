class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        if (nums.length == 0) {
            return 0;
        }    
        
        int currentMax = 0;
        int totalMax = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                currentMax++;
            }
            else {
                totalMax = Math.max(totalMax, currentMax);
                currentMax = 0;
            }
        }
        
        return Math.max(totalMax, currentMax);
    }
}
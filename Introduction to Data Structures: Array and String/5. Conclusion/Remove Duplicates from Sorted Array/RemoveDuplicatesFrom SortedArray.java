class Solution {
    public int removeDuplicates(int[] nums) {
                                  
        // Input: nums = [0,1,2,3,4,2,2,3,3,4]'
                                              
        // edge case
        if (nums.length == 0) {
            return 0;
        }
        
        if (nums.length == 1) {
            return 1;
        }
        
        int l = 1;
        int r = 1;
        
        while (r <= nums.length-1) {
            if (nums[r] != nums[r-1]) {
                nums[l] = nums[r];
                l += 1;
                r += 1;
            }
            else {
                r += 1;
            }
        }
        
        return l;
        
    }
}
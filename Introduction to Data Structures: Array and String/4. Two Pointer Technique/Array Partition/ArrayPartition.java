class Solution {
    public int arrayPairSum(int[] nums) {
        
        // Handle edge cases
        if (nums.length == 0) {
            return 0;
        }
        
        if (nums.length == 1 || nums.length == 2) {
            return nums[0];
        }
        
        // Create a variable to store the result
        int result = 0;
        
        // Sort the array
        Arrays.sort(nums);
        
        // Iterate every other element
        for (int i = 0; i < nums.length; i += 2) {
            
            // Add element to the result
            result += nums[i];
        }
        
        // Return result
        return result;
    }
}
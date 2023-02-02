class Solution {
    // create helper method to calculate right sum 
    public static int calculateRightSum(int totalSum, int leftSum, int currentVal) {
        return totalSum - leftSum - currentVal; 
    }

    // create helper method to calcuate total sum
    public static int calculateTotalSum(int [] nums) {
        int total = 0;

        for (int i = 0; i < nums.length; i++) {
            total = total + nums[i];
        }

        return total;
    }
    
    public int pivotIndex(int[] nums) {
        
        // calculate the total sum of the array 
        int totalSum = calculateTotalSum(nums);
        
        // create variable for the left sum
        int leftSum = 0;
        
        // iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // System.out.println("i: " + i);
            // System.out.println("leftSum: " + leftSum);
            // System.out.println("rightSum: " + calculateRightSum(totalSum, leftSum, nums[i]));
        
            // if the index is not zero
            if (i != 0) {
                // add current value to left sum
                leftSum = leftSum + nums[i-1];
            }
            
            // if left sum == right sum
            if (leftSum == calculateRightSum(totalSum, leftSum, nums[i])) {
                // return index
                return i;
            }
        }
        return - 1;
        
        
    }
}
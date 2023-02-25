class Solution {
    public int[] runningSum(int[] nums) {

        if (nums.length == 1) {
            return nums;
        }

        int curSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            nums[i] += curSum;
            curSum = nums[i];
        }

        return nums;
    }
}
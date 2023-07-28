class Solution {
    public int[] productExceptSelf(int[] nums) {

        int L = nums.length;

        int[] result = new int[L];

        int factor = 1;

        // Going forward
        for (int i = 0; i < L; i++) {

            result[i] = factor;

            factor *= nums[i];
        }

        // Going backwards
        factor = 1;

        for (int i = L - 1; i > -1; i--) {
            result[i] *= factor;

            factor *= nums[i];
        }

        return result;

    }
}
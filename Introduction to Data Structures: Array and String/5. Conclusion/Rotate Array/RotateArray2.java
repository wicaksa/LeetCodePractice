class Solution {
    public void rotate(int[] nums, int k) {
        
        // handle if k is larger than the size of the input
        if (k > nums.length) {
            k = k % nums.length;   
        }
    
        // nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4]
        // nums = [7,6,5,4,3,2,1]
        reverseArray(0, nums.length - 1, nums);
        
        // nums = [5,6,7,4,3,2,1]
        reverseArray(0, k - 1, nums);
        
        // nums = [5,6,7,1,2,3,4]
        reverseArray(k, nums.length - 1, nums);
    }
    
    // given the indices and array, it will reverse it in place
    private void reverseArray(int left, int right, int[]nums) {
        int temp;
        while (left <= right) {
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            left++;
            right--;
        }
    }
}
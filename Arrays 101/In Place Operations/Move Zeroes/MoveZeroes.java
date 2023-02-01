/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
*/

class Solution {
    public void moveZeroes(int[] nums) {

        // edge case: length is 0 or 1 just return
        if (nums.length > 1) {
            // create left and right pointer
            int l = 0;
            int r = 0;
            int temp;

            // while right pointer is less than nums.length
            while (r < nums.length) {
                // if the right pointer is pointing to a zero
                if (nums[r] == 0) {

                    // increment right pointer
                    r++;
                } else {
                    // else : right pointer is not pointing to a zero

                    // swap elements at left pointer with right pointer
                    temp = nums[l];
                    nums[l] = nums[r];
                    nums[r] = temp;

                    // increment left pointer and right pointer
                    l++;
                    r++;
                }
            }
        }
    }
}
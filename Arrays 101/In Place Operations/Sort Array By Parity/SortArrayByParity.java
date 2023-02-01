/*
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
    
        e
nums = [3,1,2,4]
        o
*/

class Solution {
    public int[] sortArrayByParity(int[] nums) {

        // edge case: length of nums is 0 or 1
        int l = nums.length;
        if (l < 2) {
            return nums;
        }

        // create two pointers : even, odd
        int even = 0;
        int odd = 0;
        int temp; // used for swap

        // while even pointer < length of nums
        while (even < l) {

            // if even pointer is at an odd element
            if (nums[even] % 2 != 0) {

                // increment pointer
                even++;
            } else {
                // else even pointer is at an even element

                // swap
                temp = nums[odd];
                nums[odd] = nums[even];
                nums[even] = temp;

                // increment both pointers
                even++;
                odd++;
            }
        }
        // return nums
        return nums;
    }
}
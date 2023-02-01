// Two pointer approach using a read and write pointer.

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

// Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

// Return k after placing the final result in the first k slots of nums.

// Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

// nums = [0,0,1,1,1,2,2,3,3,4]

class Solution {
    public int removeDuplicates(int[] nums) {
        // edge case: if nums length is nul;
        if (nums == null) {
            return 0;
        }
        // create a write pointer starting at index one
        int writePointer = 1;

        // iterate using a read pointer starting at index 1
        for (int readPointer = 1; readPointer < nums.length; readPointer++) {

            // if current element doesn't equal the previous element
            if (nums[readPointer] != nums[readPointer - 1]) {

                // set value at writePointer to value at readPointer
                nums[writePointer] = nums[readPointer];

                // increment write pointer
                writePointer++;
            }
        }
        // return writePointer
        return writePointer;
    }
}
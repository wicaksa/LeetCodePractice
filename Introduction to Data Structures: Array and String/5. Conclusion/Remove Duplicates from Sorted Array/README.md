# Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## Approach

For this problem, we used a two poiner approach. One pointer will be a read pointer and the other will be a write pointer. The read pointer will move forward unitl it reaches a new number. Then, the write pointer will write that value at the current index before both pointers are incremented. This will continue until the read pointer goes out of bounds.

## Complexity

### Space Complexity

O(1) since our algorithm deals with the array in place.

### Time Complexity

O(N) since we are doing this problem in one pass.

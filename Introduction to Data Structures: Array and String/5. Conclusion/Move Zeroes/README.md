# Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## Approach

This approach was similar to my previous implementation. Essentially, we want to move all the zeroes to the back and the non zeroes to the front without messing up the order. To do this, we will have two pointers. One read and one write. The read pointer will check to see if it's on a non zero number. If it is, it will swap values with the write pointer before both pointers get incremented.

## Complexity

### Time

O(N) This problem is done in linear time with one for loop.

### Space

O(1) This problem is done in constant space thus not needing extra space to store the answer.

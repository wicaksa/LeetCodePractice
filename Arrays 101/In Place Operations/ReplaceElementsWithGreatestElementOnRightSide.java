// Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

// After doing so, return the array.

class Solution {
    public int[] replaceElements(int[] arr) {
        // input : integer array
        // output: integer array

        // edge case: if length of array is less than 2 ([])
        if (arr.length == 0) {
            return arr;
        }

        if (arr.length == 1) {
            arr[0] = -1;
        }

        // create temp variable to store current element
        int tempVal;
        // set max value to last element
        int maxVal = arr[arr.length - 1];

        // set last element to -1
        arr[arr.length - 1] = -1;

        // iterate from second to last element
        for (int i = arr.length - 2; i >= 0; i--) {

            // set temp value to current value
            tempVal = arr[i];

            // set the current value to max value
            arr[i] = maxVal;

            // check if temp value > max value
            if (tempVal > maxVal) {

                // set temp value to max value
                maxVal = tempVal;
            }
        }
        // return the array
        return arr;
    }
}
class Solution {
    public boolean checkIfExist(int[] arr) {
        // input : integer array
        // output: boolean value

        // edge case : if array is of length 0 or [0]
        if (arr.length < 2) {
            return false;
        }

        // iterate through the array
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                // if there is a value that is 2 * current array
                // if the index of that value != current index
                if (arr[j] == arr[i] * 2 && i != j) {
                    // return true
                    return true;
                }
            }
        }
        // return false
        return false;

    }
}
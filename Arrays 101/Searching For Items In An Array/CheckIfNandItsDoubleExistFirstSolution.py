# Given an array arr of integers, check if there exist two indices i and j such that :

#     i != j
#     0 <= i, j < arr.length
#     arr[i] == 2 * arr[j]

# This solution runs
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # input : int array
        # output: boolean if there are two indices where arr[i] == arr[j] * 2

        # edge case if arr length is 0 or if there is one element and the element is 0
        if len(arr) == 0 or arr == [0]:
            return False

        # iterate through the array
        for i in range(0, len(arr)):

            # if there exists an element that is 2 * current element
            if arr.count(2*arr[i]) > 0:

                # if the index is different #[0,34,55,0,55]
                if arr.index(2*arr[i]) != i:

                    # return true
                    return True

        # return false
        return False

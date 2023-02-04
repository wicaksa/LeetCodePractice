class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # input : int array
        # output: int array

        # increment the large integer by one and return the resulting array of digits.

        # edge case: digits length is 0
        if len(digits) == 0:
            return nums

        # create a counter for 1
        oneCount = 1

        # create a pointer
        p = len(digits) - 1

        # iterate from the last index while counter == 1 and pointer > -1
        while oneCount == 1 and p > -1:

            # add 1 to the element
            digits[p] += 1

            # decrement one count
            oneCount -= 1

            # if the element becomes a 10
            if digits[p] == 10:

                # change element to 0
                digits[p] = 0

                # inc 1 to the counter
                oneCount += 1

                # decrement pointer
                p -= 1

        # insert 1 at 0 index if oneCount = 1
        if oneCount == 1:
            digits.insert(0, 1)

        # return digits
        return digits

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # handle edge cases:
        if len(nums) == 0:
            return 0

        # create two pointers both starting at the last index
        # one pointer will look for k values
        # the other will stay in place until value is swapped
        l = len(nums) - 1
        r = len(nums) - 1

        # create a counter to keep track of the number of removals
        numOfRemovals = 0

        # iterate the finder pointer until it reaches the beginning of the array
        while l >= 0:

            # if the left pointer finds val
            print(nums[l] == val)
            if nums[l] == val:

                # swap
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                # increment removals
                numOfRemovals += 1

                # decrement left pointer
                l -= 1

                # decrement the other pointer
                r -= 1

            # else if finder pointer doesn't equal val
            else:

                # decrement left pointer
                l -= 1

        # return length of nums - number of removals to get the remaining values
        return len(nums) - numOfRemovals

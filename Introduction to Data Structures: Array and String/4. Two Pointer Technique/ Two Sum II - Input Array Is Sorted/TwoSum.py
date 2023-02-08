class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # approach 1: timed out (18/22 test cases passed)
        """

        # iterate through numbers
        for i in range(0, len(numbers)-1):

            # iterate from numbers + 1 until the end of the list 
            for j in range(i+1, len(numbers)):

                # if target - first number = second number
                if numbers[j] == target - numbers[i]:

                    # return [first index + 1, second index + 1]
                    return [i+1, j+1]
        """

        # approach 2: implement a binary search for second element
        """
        
        # iterate through numbers
        for i in range(0, len(numbers)-1):
        
            # get target number 
            findValue = target - numbers[i]
            
            # create left and right pointers
            left = i+1
            right= len(numbers)-1

            # binary search for the right number
            while left <= right:
                
                mid  = (left + right) // 2
                
                print(left, right, mid, findValue, numbers[mid])
            
                if findValue < numbers[mid]:
                    right = mid - 1
                
                elif findValue > numbers[mid]:
                    left = mid + 1
                    
                else: # found
                    return [i+1, mid+1]
        
        """

        # approach 3: use two pointers

        # create two pointers one at each end of the list
        l = 0
        r = len(numbers) - 1

        # iterate the list while left pointer <= right pointer
        while l <= r:

            # find the sum of the elements at both pointers
            # if the sum > target
            if numbers[l] + numbers[r] > target:

                # move the right pointer left since these are larger values
                r -= 1

            # else if the sum < target
            elif numbers[l] + numbers[r] < target:

                # move left pointer right since these are smaller values
                l += 1

            # else the sum equals the target
            else:

                # return left pointer + 1 and right pointer + 1
                return [l+1, r+1]

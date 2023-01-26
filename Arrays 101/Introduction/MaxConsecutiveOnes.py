# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # input : integer array
        # output: integer representing the maximum number of consecutive 1's
        
        # create a variable to store the max result
        maxResult = 0
        
        # create a variable to store current result
        currentResult = 0
        
        # iterate through the array
        for i in range(0, len(nums)):
        
            # if the number is a 1
            if nums[i] == 1:
            
                # add 1 to the current result variable 
                currentResult += 1
            
            # if the number is 0 
            else:
            
                # check if the current result is greater than the max result
                
                # if the current result > max result 
                if currentResult > maxResult:
                    
                    # set current result to max result 
                    maxResult = currentResult
            
                # reset the current result variable to 0
                currentResult = 0
                
        # if current result > max result
        if currentResult > maxResult:
            # return current result 
            return currentResult
                
        # return the max result 
        return maxResult
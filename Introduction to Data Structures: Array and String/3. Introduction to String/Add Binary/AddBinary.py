class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # initialize an empty string to store the result
        result = ""
        
        # first figure out how to get the sum of binary    
        def calcSum(arr):
            power = 0
            total = 0
            
            for i in range(len(arr)-1, -1, -1):
                if arr[i] == '1': 
                    total = total + 2 ** power
                power += 1
            return total
        
        # calculate the sum of the input
        total = calcSum(a) + calcSum(b)
        
        # edge case if the sum is 0
        if total == 0: 
            return "0"
        
        # testing for exponents fromm 100 to 0
        p = 100
       
        while p > -1: 
            
            # if the total is greater than or equal to 2^p 
            if total >= (2 ** p): 
                
                # divide and get the remainder
                total = total % (2 ** p)
                
                # if the remainder is not 0
                if total >= 0:
                    
                    # add a '1' to the result string
                    result += "1"
                
                # else if the remainder is 0
                else: 
                    
                    # just append a '0' to the result
                    result += "0"
            
            # else if the total is 0 (no more divisions) and the total is less than 2^p
            elif (total == 0) and total < (2 ** p):
                
                # add '0' to the result
                result += "0"
            
            # for adding 0's in the middle of result
            else: 
                # check if the result string is not empty
                if len(result) != 0:
                    # add a 0
                    result += "0"
                # if the string is empty, don't do anything bc they are leading '0's
                # not part of solution
            
            # decrement p
            p -= 1

        return result
            
            
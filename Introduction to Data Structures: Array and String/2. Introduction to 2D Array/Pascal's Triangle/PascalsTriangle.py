class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # create an empty array to store result
        result = []
        
        # iterate through the number of rows 
        for i in range(0, numRows):
        
            # create a temporary array 
            temp = []
            
            # iterate through the current number of rows
            for j in range(0, i+1):
                
                # if index is 0 or last append 1
                if (j == 0 or j== i):
                    total = 1
                
                else: 
                    # calculate the sum of the two numbers above
                    total = result[i-1][j-1] + result[i-1][j]
                
                # append number to temporary array
                temp.append(total)
            
            # append temporary array to result array
            result.append(temp)
        
        # return result array
        return result
        
       
        
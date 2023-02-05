class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # input : 2 strings
        # output: integer
        
        # edge case where needle or haystack are 0
        if (len(haystack) == 0) or (len(needle) == 0) or (len(needle) > len(haystack)):
            return -1
        
        # edge case where the lengths of both are equal
        if len(haystack) == len(needle):
            print("test")
            if haystack == needle: 
                return 0
            else:
                return -1
        
        # get the length of needle and use it as a sliding window 
        window = len(needle)
        
        # iterate from 0 to haystack length - length of needle 
        for i in range(0, len(haystack) - window + 1):
            
            print("haystack substring: ", haystack[i:i+window])
        
            # if substring in haystack equals needle
            if haystack[i:i+window] == needle:
            
                # return the beginning index
                return i
                
        # did not find so return -1
        return -1
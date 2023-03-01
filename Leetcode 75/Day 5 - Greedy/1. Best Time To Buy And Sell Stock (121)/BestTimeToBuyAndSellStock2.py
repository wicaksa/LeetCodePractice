class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if the right pointer is greater than the left
        # find the difference
        # check if the difference is greater than the max profit

        # if the right pointer is less than or equal the left
        # move the left pointer to the right pointer location

        # move the right pointer

        l = 0
        r = 0
        maxProfit = 0

        while (r < len(prices)):
            if (prices[r] > prices[l]):
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit

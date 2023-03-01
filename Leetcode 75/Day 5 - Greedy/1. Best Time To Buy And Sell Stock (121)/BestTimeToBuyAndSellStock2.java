class Solution {
    public int maxProfit(int[] prices) {

        int max_profit = 0;
        int l = 0;
        int r = 0;

        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                max_profit = Math.max(max_profit, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return max_profit;
    }
}
class Solution {
    public int maxProfit(int[] prices) {
        // input : array of prices
        // output: int representing the maximum profit

        int cheapestPrice = (int) Math.pow(10, 5) + 1;
        int maximumProfit = 0;
        int currentProfit;

        for (int p : prices) {
            if (p < cheapestPrice) {
                cheapestPrice = p;
            } else {
                currentProfit = p - cheapestPrice;
                maximumProfit = Math.max(currentProfit, maximumProfit);
            }
        }
        return maximumProfit;
    }
}
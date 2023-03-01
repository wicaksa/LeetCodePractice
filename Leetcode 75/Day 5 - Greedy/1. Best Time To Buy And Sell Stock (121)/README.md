# Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Example

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

## Constraints

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

## Approach
1. The first approach uses one pointer that traverses the array. At each iteration, we check whether the value is smaller, or greater than or equal to the value stored in the minimumValue variable. If it is smaller. we simply update the value as the smallest value. Otherwise, we calculate the difference between the current value and the smallest value seen. Then we update the maximumProfit value by comparing it to the diffence we just calculated. At the end of the iteration, we simply return the maximumProfit.

2. The second approach requires two pointers, a left and a right. At each iteration, we check whether the value at the right pointer is greater than the value of the left pointer. If it is, we can calculate the difference and update the maximum profit. If else, we simply move the left pointer to the location of the right pointer because now the left pointer will have the smallest value seen. We simply update the right pointer after doing this check. After the loop exits, we simply return the maximum profit variable.

## Review & Evaluate
1. Time : O(N) Space: O(N)
2. Time : O(N) Space: O(N)
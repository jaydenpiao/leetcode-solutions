package solutions_java.arrays;
/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int bestPrice = prices[0];
        int maxProfit = 0;
        for (int price : prices) {
            if (price - bestPrice > maxProfit) {
                maxProfit = price - bestPrice;
            }
            if (price < bestPrice) {
                bestPrice = price;
            }
        }
        return maxProfit;
    }
}
// @lc code=end


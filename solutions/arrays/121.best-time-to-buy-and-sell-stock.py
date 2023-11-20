#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        res = 0

        for price in prices[1:]:
            if price - min > res:
                res = price - min
            if price < min:
                min = price
        return res
        
# @lc code=end


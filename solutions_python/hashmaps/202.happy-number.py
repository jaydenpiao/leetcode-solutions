#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while n > 0:
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n = n / 10
            if res in seen:
                return False
            if res == 1:
                return True
            seen.append(res)
            n = res
        return False
        
# @lc code=end


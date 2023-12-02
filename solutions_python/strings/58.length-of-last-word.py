#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = len(s)-1
        res = 0

        while idx >= 0:
            if s[idx] != " ":
                res += 1
            if res > 0 and s[idx] == " ":
                return res
            idx -= 1
        return res
        
# @lc code=end


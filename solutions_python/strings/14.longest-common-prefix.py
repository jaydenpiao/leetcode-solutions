#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return res
        
        shortest = strs[0]
        for str in strs:
            if len(str) < len(shortest):
                shortest = str
        
        for i in range(len(shortest)):
            curr = shortest[i]
            for str in strs:
                if str[i] != curr:
                    return res
            res += curr
        return res
        
        
# @lc code=end


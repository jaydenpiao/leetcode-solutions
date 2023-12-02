#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s_idx = 0
        
        for i in range(len(t)):
            if s[s_idx] == t[i]:
                s_idx += 1
                if s_idx == len(s):
                    return True
                
        return False
        
# @lc code=end


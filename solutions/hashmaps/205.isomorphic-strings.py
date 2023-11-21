#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mydict = {}
        for i in range(len(s)):
            if s[i] not in mydict:
                mydict[s[i]] = t[i]
            elif mydict[s[i]] != t[i]:
                return False
        if len(set(s)) != len(set(t)):
            return False
        return True
        
# @lc code=end


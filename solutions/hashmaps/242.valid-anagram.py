#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mydict = {}
        for i in range(len(s)):
            if s[i] not in mydict:
                mydict[s[i]] = 1
            else:
                mydict[s[i]] += 1
        
        for char in t:
            if char not in mydict:
                return False
            else:
                mydict[char] -= 1
                if mydict[char] < 0:
                    return False
        return True
        
# @lc code=end


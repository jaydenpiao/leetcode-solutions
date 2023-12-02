#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        string = ""
        end = len(s) - 1
        while end >=0:
            string += s[end]
            end -= 1
        
        res = romandict[string[0]]
        
        for i in range(1, len(string)):
            if romandict[string[i]] >= romandict[string[i-1]]:
                res += romandict[string[i]]
            else:
                res -= romandict[string[i]]
        return res


        
# @lc code=end


#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mylist = s.split()
        if len(pattern) != len(mylist):
            return False
        
        mydict = {}
        for i in range(len(pattern)):
            if pattern[i] not in mydict:
                mydict[pattern[i]] = mylist[i]
            elif mydict[pattern[i]] != mylist[i]:
                return False
        if len(set(pattern)) != len(set(mylist)):
            return False
        return True
    
        
# @lc code=end


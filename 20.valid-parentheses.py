#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        mylist = []
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False
        for char in s:
            if char == "}" or char == ")" or char == "]":
                if len(mylist) == 0:
                    return False
                if mylist.pop() != mydict[char]:
                    return False
            else:
                mylist.append(char)
        if len(mylist) != 0:
            return False
        return True
            

        
# @lc code=end


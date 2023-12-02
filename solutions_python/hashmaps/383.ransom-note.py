#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mydict = {}

        for char in magazine:
            if char not in mydict:
                mydict[char] = 1
            else:
                mydict[char] += 1
        
        for char in ransomNote:
            if char not in mydict:
                return False
            else:
                mydict[char] -= 1
                if mydict[char] < 0:
                    return False
                
        return True

        
# @lc code=end


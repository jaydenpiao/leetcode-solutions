#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = (''.join((i.lower()) for i in s if i.isalnum()))

        if (s[0::] == s[::-1]):
            return True
        return False

        
# @lc code=end


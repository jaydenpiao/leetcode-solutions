#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elems = 0
        for num in nums:
            if elems < 2 or num != nums[elems-2]:
                nums[elems] = num
                elems += 1
        return elems
# @lc code=end


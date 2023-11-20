#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elems = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[elems] = nums[i]
                elems += 1
        return elems

        
# @lc code=end


#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mydict = {}
        for i in range(len(nums)):
            if nums[i] not in mydict:
                mydict[nums[i]] = i
            elif abs(i - mydict[nums[i]]) <= k:
                return True
            mydict[nums[i]] = i
        return False
# @lc code=end


#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        if not nums:
            return
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                end = nums[i]
            else:
                if start == end:
                    ret.append(str(start))
                else:
                    ret.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
            
        if start == end:
            ret.append(str(start))
        else:
            ret.append(str(start) + "->" + str(end))
                   
        return ret

            


# @lc code=end


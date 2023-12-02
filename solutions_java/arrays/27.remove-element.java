/*
 * @lc app=leetcode id=27 lang=java
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            if (nums[start] == val) {
                while (start<end && nums[end] == val) {
                    end--;
                }
                nums[start] = nums[end];
                end--;
            }
            start++;
        }
        return end+1;
    }

}
// @lc code=end


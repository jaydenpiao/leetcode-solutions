/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int start = 0;
        int end = nums.length-1;
        while (start <= end) {
            if (!set.contains(nums[start])) {
                set.add(nums[start]);
                start++;
            } else {
                while (set.contains(nums[end]) && start < end) {
                    end--;
                }
                nums[start] = nums[end];
                end--;
            }
        }
        Arrays.sort(nums, 0, set.size());
        return end + 1;
    }
}
// @lc code=end


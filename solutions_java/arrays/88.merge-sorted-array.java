package solutions_java.arrays;
/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int nIdx = m; nIdx < m + n; nIdx++) {
            nums1[nIdx] = nums2[nIdx - m];
        }
        Arrays.sort(nums1);
    }
}
// @lc code=end


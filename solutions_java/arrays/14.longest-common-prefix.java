/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        int resIdx = 0;
        
        Arrays.sort(strs);
        for (int i=0; i<strs[0].length(); i++) {
            if (strs[0].charAt(i) == strs[strs.length-1].charAt(i)) {
                resIdx++;
            } else {
                break;
            }
        }
        return strs[0].substring(0,resIdx);
        
    }
}
// @lc code=end


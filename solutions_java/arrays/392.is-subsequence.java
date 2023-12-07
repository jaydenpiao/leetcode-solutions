/*
 * @lc app=leetcode id=392 lang=java
 *
 * [392] Is Subsequence
 */

// @lc code=start
class Solution {
    public boolean isSubsequence(String s, String t) {
        int sLen = s.length();
        int tLen = t.length();

        if (sLen < 1) return true;
        int sIdx = 0;
        int tIdx = 0;

        while (tIdx < tLen) {
          if (s.charAt(sIdx) == t.charAt(tIdx)) {
            sIdx++;
          }
          tIdx++;
          if (sIdx == sLen) return true;
        }
        return false;
    }
}
// @lc code=end


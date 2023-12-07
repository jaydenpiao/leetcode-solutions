package solutions_java.arrays;
/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        s = s.trim();

        for (int i = s.length()-1; i>=0; i--) {
          if (s.charAt(i) == ' ') {
            return res;
          }
          res += 1;
        }
        return res;
    }
}
// @lc code=end


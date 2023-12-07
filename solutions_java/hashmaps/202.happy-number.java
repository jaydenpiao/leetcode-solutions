package solutions_java.hashmaps;
/*
 * @lc app=leetcode id=202 lang=java
 *
 * [202] Happy Number
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        set.add(n);

        while (n != 1) {
            int copy = n;
            int res = 0;
            while (copy != 0) {
                res += (copy % 10) * (copy % 10);
                copy = copy / 10;
            }
            if (set.contains(res)) return false;
            set.add(res);
            n = res;
        }
        return true;
    }
}
// @lc code=end


package solutions_java.arrays;
/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 */

import java.util.HashMap;
import java.util.Map;

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num)+1);
            }
            if (map.get(num) > (nums.length / 2)) {
                return num;
            }
        }
        return -1;
    }
}
// @lc code=end


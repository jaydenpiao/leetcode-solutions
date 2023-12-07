package solutions_java.hashmaps;
/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i<nums.length; i++) {
          if (!map.containsKey(nums[i])) {
            map.put(target-nums[i], i);
          } else {
            return new int[]{map.get(nums[i]),i};
          }
        }
        return new int[]{};
    }
}
// @lc code=end


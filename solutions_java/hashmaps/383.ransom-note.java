package solutions_java.hashmaps;
/*
 * @lc app=leetcode id=383 lang=java
 *
 * [383] Ransom Note
 */

// @lc code=start
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0; i<magazine.length(); i++) {
            if (!map.containsKey(magazine.charAt(i))) {
                map.put(magazine.charAt(i), 1);
            } else {
                map.put(magazine.charAt(i), map.get(magazine.charAt(i))+1);
            }
        }
        for (int i=0; i<ransomNote.length(); i++) {
          if (map.containsKey(ransomNote.charAt(i)) && map.get(ransomNote.charAt(i))>0){
            map.put(ransomNote.charAt(i), map.get(ransomNote.charAt(i))-1);
          } else {
            return false;
          }
        }
        return true;
    }
}
// @lc code=end


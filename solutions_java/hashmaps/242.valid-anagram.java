package solutions_java.hashmaps;
/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> map = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            char sChar = s.charAt(i);
            if (!map.containsKey(sChar)) {
                map.put(sChar, 1);
            } else {
                map.put(sChar, map.get(sChar)+1);
            }
        }
        for (int i=0; i<t.length(); i++) {
            char tChar = t.charAt(i);
            if (map.containsKey(tChar) && map.get(tChar) > 0) {
                map.put(tChar, map.get(tChar)-1);
            } else {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end


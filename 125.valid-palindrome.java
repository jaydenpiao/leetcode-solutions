/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();

        List<Character> list = new ArrayList<>();
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                list.add(c);
            }
        }

        for (int i=0; i<list.size()/2; i++) {
            if (list.get(i) != list.get(list.size()-1-i)) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put(']','[');
        map.put('}','{');
        map.put(')','(');

        Stack<Character> stack = new Stack<>();
        for (int i=0; i<s.length(); i++) {
            char w = s.charAt(i);
            if (w==']' || w=='}' || w==')') {
                if (stack.empty() || stack.pop() != map.get(w)) return false;
            } else {
              stack.push(w);
            }
        }
        if (stack.empty()) return true;
        return false;
    }
}
// @lc code=end


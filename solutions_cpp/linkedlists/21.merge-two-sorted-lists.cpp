/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1 && !list2) return list1;
        if (!list1) return list2;
        if (!list2) return list1;

        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;

        while (list1 || list2) {
            if (!list1) {
                curr->next = list2;
                break;
            }
            if (!list2) {
                curr->next = list1;
                break;
            }
            if (list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }
        return dummy->next;
    }
};
// @lc code=end


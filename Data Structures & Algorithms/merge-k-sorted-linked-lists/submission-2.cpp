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

struct compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> currs;
        for (ListNode* node : lists) {
            if (node) {
                currs.push(node);
            }
        }
        ListNode* sorted = new ListNode(0);
        ListNode* curr = sorted;
        while (!currs.empty()) {
            ListNode* min = currs.top();
            currs.pop();
            curr->next = min;
            curr = curr->next;
            if (min->next) {
                currs.push(min->next);
            }
        }
        return sorted->next;
    }
};

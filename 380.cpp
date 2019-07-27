/**
 * Definition of singly-linked-list:
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *        this->val = val;
 *        this->next = NULL;
 *     }
 * }
 */
#include <bits/stdc++.h>
using namespace std;
class ListNode {
public:
  int val;
  ListNode *next;
  ListNode(int val) {
    this->val = val;
    this->next = NULL;
  }
};

class Solution {
public:
  /**
   * @param headA: the first list
   * @param headB: the second list
   * @return: a ListNode
   */
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    // write your code here
    int l1, l2;
    ListNode *cA, *cB, *insct;
    for (l1 = 0, cA = headA; cA; cA = cA->next, l1++)
      ;
    for (l2 = 0, cB = headB; cB; cB = cB->next, l2++)
      ;
    if (l1 == 0 || l2 == 0)
      return NULL;
    cA = headA;
    cB = headB;
    if (l1 < l2) {
      for (; l2 > l1; cB = cB->next, l2--)
        ;
    } else {
      for (; l1 > l2; cA = cA->next, l1--)
        ;
    }
    insct = NULL;
    for (; cA && cB; cA = cA->next, cB = cB->next) {
      if (cA->val == cB->val) {
        if (!insct)
          insct = cA;
      } else
        insct = NULL;
    }
    return insct;
  }
};

int main() {
  ListNode *h = new ListNode(1);
  h->next = new ListNode(2);
  h->next->next = new ListNode(3);
  h->next->next->next = new ListNode(4);
  ListNode *j = new ListNode(0);
  j->next = h->next->next;
  cout << (Solution().getIntersectionNode(h, j))->val << '\n';
}
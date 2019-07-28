#include <bits/stdc++.h>
using namespace std;
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
   * @param head: The head of linked list.
   * @return: nothing
   */
  void reorderList(ListNode *head) {
    // write your code here
    if (!head)
      return;
    ListNode *curr, *l, *r, *temp, *lex, *rex;
    int len, idx;
    for (curr = head, len = 0; curr; len++)
      curr = curr->next;
    if (len < 3)
      return;
    for (idx = 0, curr = head; idx < (len - 1) / 2; idx++)
      curr = curr->next;
    l = curr;
    r = curr->next;
    l->next = NULL;
    while (r) {
      temp = r->next;
      r->next = l;
      l = r;
      r = temp;
    }
    for (lex = head, rex = l, idx = 0; idx <= (len - 1) / 2; idx++) {
      l = lex->next;
      lex->next = rex;
      r = rex->next;
      rex->next = l;
      lex = l;
      rex = r;
    }
  }
};
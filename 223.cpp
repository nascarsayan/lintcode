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
   * @param head: A ListNode.
   * @return: A boolean.
   */
  bool isPalindrome(ListNode *head) {
    // write your code here
    int len, i;
    ListNode *curr, *l, *r, *temp, *rex;
    if (!head)
      return true;
    if (!head->next)
      return true;
    if (!head->next->next)
      return (head->val == head->next->val);
    for (len = 0, curr = head; curr; len++)
      curr = curr->next;
    for (i = 0, curr = head; i < (len - 1) / 2; i++)
      curr = curr->next;
    l = curr;
    r = curr->next;
    while (r) {
      temp = r->next;
      r->next = l;
      l = r;
      r = temp;
    }
    for (curr = head, rex = l, i = 0; i <= (len - 1) / 2;
         curr = curr->next, rex = rex->next, i++)
      if (curr->val != rex->val)
        return false;
    return true;
  }
};
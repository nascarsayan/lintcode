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
   * @param head: the List
   * @param k: rotate to the right k places
   * @return: the list after rotation
   */
  ListNode *rotateRight(ListNode *head, int k) {
    // write your code here
    ListNode *curr, *newh;
    int len, idx;
    if (k == 0 || !head || !(head->next))
      return head;
    for (curr = head, len = 0; curr; len++)
      curr = curr->next;
    k %= len;
    if (k == 0)
      return head;
    for (curr = head, idx = 0; idx <= len - k - 2; idx++)
      curr = curr->next;
    newh = curr->next;
    curr->next = NULL;
    curr = newh;
    while (curr->next)
      curr = curr->next;
    curr->next = head;
    return newh;
  }
};
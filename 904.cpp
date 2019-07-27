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
   * @param head: the first Node
   * @return: the answer after plus one
   */
  int checkAdd(ListNode *head) {
    int newdig = head->val + 1;
    if (newdig <= 9) {
      head->val = newdig;
      return 0;
    }
    head->val = 0;
    return 1;
  }

  int recurse(ListNode *head) {
    if (!head->next) {
      return checkAdd(head);
    }
    int carry = recurse(head->next);
    if (carry > 0) {
      return checkAdd(head);
    }
  }

  ListNode *plusOne(ListNode *head) {
    // Write your code here
    if (!head)
      return head;
    int carry = recurse(head);
    if (carry > 0) {
      ListNode *temp = new ListNode(1);
      temp->next = head;
      head = temp;
    }
    return head;
  }
};
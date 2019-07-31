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
   * @param head: head is the head of the linked list
   * @return: head of the linked list
   */
  ListNode *deleteDuplicates(ListNode *head) {
    // write your code here
    ListNode *curr, *stub = new ListNode(0), *temp;
    stub->next = head;
    curr = stub;
    while (curr->next && curr->next->next) {
      if (curr->next->val == curr->next->next->val) {
        temp = curr->next->next;
        while (temp->next && temp->next->val == curr->next->val)
          temp = temp->next;
        curr->next = temp->next;
      } else
        curr = curr->next;
    }
    return stub->next;
  }
};
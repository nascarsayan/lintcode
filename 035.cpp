/**
 * Definition of singly-linked-list:
 *
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
   * @param head: n
   * @return: The new head of reversed linked list.
   */
  ListNode *reverse(ListNode *head) {
    // write your code here
    if (head == NULL || head->next == NULL)
      return head;
    ListNode *stub = new ListNode(0);
    stub->next = head;
    ListNode *left = stub, *right = stub->next, *temp;
    while (right != NULL) {
      temp = right->next;
      right->next = left;
      left = right;
      right = temp;
    }
    head->next = NULL;
    delete stub;
    head = left;
    return head;
  }
};
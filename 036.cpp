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
   * @param head: ListNode head is the head of the linked list
   * @param m: An integer
   * @param n: An integer
   * @return: The head of the reversed ListNode
   */
  ListNode *reverseBetween(ListNode *head, int m, int n) {
    int idx;
    ListNode *stub = new ListNode(0), *inode, *lex, *left, *right, *temp, *rex;
    stub->next = head;
    for (inode = stub, idx = 0; idx < m - 1; inode = inode->next, idx++)
      ;
    lex = inode;
    for (idx++, left = lex->next, right = left->next; idx < n; idx++) {
      temp = right->next;
      right->next = left;
      left = right;
      right = temp;
    }
    temp = lex->next;
    lex->next = left;
    temp->next = right;
    return stub->next;
  }
};

int main() {
  ListNode *head = new ListNode(10);
  head->next = new ListNode(20);
  head->next->next = new ListNode(30);
  head->next->next->next = new ListNode(40);
  head->next->next->next->next = new ListNode(50);
  Solution().reverseBetween(head, 3, 4);
  for (ListNode *inode = head; inode != NULL; inode = inode->next)
    printf("%d -> ", inode->val);
  printf("NULL\n");
  return 0;
}
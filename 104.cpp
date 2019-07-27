/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
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
   * @param lists: a list of ListNode
   * @return: The head of one sorted list.
   */
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    // write your code here
    int minInd, i, len = lists.size(), currl;
    vector<ListNode *> heads;
    ListNode *newlist = new ListNode(0);
    ListNode *newhead = newlist;
    currl = len;
    for (i = 0; i < len; i++) {
      if (lists[i])
        heads.push_back(lists[i]);
      else
        currl--;
    }
    while (currl > 0) {
      minInd = 0;
      for (i = 1; i < currl; i++) {
        if (heads[i]->val < heads[minInd]->val)
          minInd = i;
      }
      newhead->next = heads[minInd];
      newhead = newhead->next;
      heads[minInd] = heads[minInd]->next;
      newhead->next = NULL;
      if (!heads[minInd]) {
        heads.erase(heads.begin() + minInd);
        currl -= 1;
      }
    }
    return newlist->next;
  }
};

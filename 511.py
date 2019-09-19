"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
  """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

  def swapNodes(self, head, v1, v2):
    # write your code here
    if v1 == v2:
      return head
    loc = {}
    curr = head
    while (curr):
      if curr.val == v1:
        loc[v1] = curr
      if curr.val == v2:
        loc[v2] = curr
      curr = curr.next
    if v1 in loc and v2 in loc:
      loc[v1].val, loc[v2].val = v2, v1
    return head

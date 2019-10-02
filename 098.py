"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class Solution:
  """
  @param head: The head of linked list.
  @return: You should return the head of the sorted linked list, using constant space complexity.
  """

  def sortList(self, head):
    # write your code here
    def msort(head):
      if head is None or head.next is None:
        return head
      size, curr = 0, head
      while (curr):
        size += 1
        curr = curr.next
      mid = size // 2
      curr, cnt = head, 0
      while (cnt < mid - 1):
        cnt += 1
        curr = curr.next
      rhead, curr.next = curr.next, None
      lhead = msort(head)
      rhead = msort(rhead)
      lc, rc, curr = lhead, rhead, ListNode(None)
      nhead = curr
      while (lc and rc):
        if lc.val < rc.val:
          curr.next, lc = lc, lc.next
        else:
          curr.next, rc = rc, rc.next
        curr = curr.next
      if lc:
        curr.next = lc
      if rc:
        curr.next = rc
      nhead = nhead.next
      return nhead

    return msort(head)


l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(2)
l1.next, l2.next = l2, l3
l4 = Solution().sortList(l1)
while (l4):
  print(l4.val)
  l4 = l4.next

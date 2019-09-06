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
  @param head: a singly linked list
  @return: Modified linked list
  """

  def oddEvenList(self, head):
    # write your code here
    if head is None or head.next is None:
      return head
    oh, eh = head, head.next
    oc, ec = oh, eh
    while (oc and ec):
      oc.next = ec.next
      if oc.next:
        ec.next = oc.next.next
      else:
        ec.next = None
      oc = oc.next
      ec = ec.next
    if oc:
      oc.next = None
    oc = oh
    while (oc.next):
      oc = oc.next
    oc.next = eh
    return oh

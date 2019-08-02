"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
  """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

  def hasCycle(self, head):
    # write your code here
    j1 = head
    j2 = head
    if j1 is None:
      return False
    while (j2.next is not None and j2.next.next is not None):
      j1 = j1.next
      j2 = j2.next.next
      if (j1 == j2):
        return True
    return False

"""
Definition of DoublyListNode
class ListNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
  """
    @param head: the given doubly linked list
    @param nodes: the given nodes array
    @return: the number of blocks in the given array
    """

  def blockNumber(self, head, nodes):
    # write your code here
    nodes = set(nodes)
    curr, nb = head, 0
    while (curr):
      if curr.val not in nodes:
        curr = curr.next
      else:
        while (curr.next and curr.next.val in nodes):
          curr = curr.next
        curr = curr.next
        nb += 1
    return nb

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
  """
    @param head: the head
    @param G: an array
    @return: the number of connected components in G
    """

  def numComponents(self, head, G):
    # Write your code here
    curr = head
    G = set(G)
    newst = True
    while (curr):
      if curr.val in G:
        if newst:
          newst = False
        else:
          G.remove(curr.val)
      else:
        newst = True
      curr = curr.next
    return len(G)

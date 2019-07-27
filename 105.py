from collections import defaultdict
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class RandomListNode:

  def __init__(self, x):
    self.label = x
    self.next = None
    self.random = None


class Solution:

  # @param head: A RandomListNode
  # def printLL(self, head):
  #   while (head):
  #     rv = None
  #     if (head.random):
  #       rv = head.random.label
  #     print('(%d, random = %r) -> ' % (head.label, rv), end='')
  #     head = head.next

  # @param head: A RandomListNode
  # @return: A RandomListNode
  def copyRandomList(self, head):
    # write your code here
    if head is None:
      return head
    chead = head
    loc = defaultdict(RandomListNode)
    nhead = RandomListNode(chead.label)
    cnhead = nhead
    loc[id(chead)] = cnhead
    while (chead.next):
      cnhead.next = RandomListNode(chead.next.label)
      chead = chead.next
      cnhead = cnhead.next
      loc[id(chead)] = cnhead
    chead = head
    cnhead = nhead
    while (chead):
      rptr = chead.random
      if rptr is not None:
        cnhead.random = loc[id(rptr)]
      chead = chead.next
      cnhead = cnhead.next
    return nhead


# a = []
# a.append(RandomListNode(10))
# a.append(RandomListNode(30))
# a.append(RandomListNode(20))
# a[0].next = a[1]
# a[1].next = a[2]
# a[0].random = a[2]
# a[1].random = a[0]
# a[2].random = a[1]
# Solution().copyRandomList(a[0])

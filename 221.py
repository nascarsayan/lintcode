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
  @param l1: The first list.
  @param l2: The second list.
  @return: the sum list of l1 and l2.
  """

  def addLists2(self, l1, l2):
    # write your code here
    if not l1:
      return l2
    if not l2:
      return l1
    n1, n2 = [], []
    c1, c2 = l1, l2
    while (c1):
      n1.append(c1.val)
      c1 = c1.next
    while (c2):
      n2.append(c2.val)
      c2 = c2.next
    curr = None
    cry = 0
    while (n1 and n2):
      tot = n1.pop(-1) + n2.pop(-1) + cry
      curr, curr.next, cry = ListNode(tot % 10), curr, tot // 10
    while (n1):
      tot = n1.pop(-1) + cry
      curr, curr.next, cry = ListNode(tot % 10), curr, tot // 10
    while (n2):
      tot = n2.pop(-1) + cry
      curr, curr.next, cry = ListNode(tot % 10), curr, tot // 10
    if cry > 0:
      curr, curr.next, cry = ListNode(cry % 10), curr, cry // 10
    return curr

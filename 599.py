import bisect
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
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """

  def insert(self, node, x):
    # write your code here
    nodes = set()
    newn = ListNode(x)
    if node is None:
      newn.next = newn
      return newn
    if node.next == node:
      node.next, newn.next = newn, node
      return node
    curr = node
    while (True):
      ele = (curr.val, id(curr), curr)
      if ele in nodes:
        break
      nodes.add(ele)
      curr = curr.next
    nlist = list(sorted(nodes))
    idx = (bisect.bisect_right(nlist, (x, float('inf'), newn))) % (len(nlist))
    print(idx)
    print(nlist)
    nlist[idx][2].next, newn.next = newn, nlist[idx][2].next
    return newn


n4 = ListNode(10)
n3 = ListNode(9, n4)
n2 = ListNode(10, n3)
n1 = ListNode(10, n2)
n4.next = n1
x = Solution().insert(n1, 9)
for _ in range(10):
  # print(x.val)
  x = x.next

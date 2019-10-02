"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class SegmentTreeNode:

  def __init__(self, start, end, max):
    self.start, self.end, self.max = start, end, max
    self.left, self.right = None, None


class Solution:
  """
    @param A: a list of integer
    @return: The root of Segment Tree
    """

  def build(self, A):
    # write your code here
    def recurse(st, fl):
      root = SegmentTreeNode(st, fl, A[st])
      if st == fl:
        return root
      mid = (st + fl) // 2
      root.left, root.right = recurse(st, mid), recurse(mid + 1, fl)
      root.max = max(root.left.max, root.right.max)
      return root

    size = len(A)
    if size == 0:
      return None
    return recurse(0, size - 1)

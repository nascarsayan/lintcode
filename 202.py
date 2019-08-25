"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """

  def query(self, root, start, end):
    # write your code here
    def recurse(root):
      if root is None:
        return
      if root.start >= start and root.end <= end:
        maxv[0] = max(maxv[0], root.max)
        return
      if max(start, root.start) > min(end, root.end):
        return
      recurse(root.left)
      recurse(root.right)

    maxv = [float('-inf')]
    recurse(root)
    return maxv[0]

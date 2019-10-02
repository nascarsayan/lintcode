"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
  """
  @param: root: The root of segment tree.
  @param: start: start value.
  @param: end: end value.
  @return: The count number in the interval [start, end]
  """

  def query(self, root, start, end):
    # write your code here
    def recurse(root):
      if root is None:
        return 0
      if start <= root.start <= root.end <= end:
        return root.count
      if max(start, root.start) > min(end, root.end):
        return 0
      return recurse(root.left) + recurse(root.right)

    return recurse(root)

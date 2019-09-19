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
    @param index: index.
    @param value: value
    @return: nothing
    """

  def modify(self, root, index, value):
    # write your code here
    def recurse(root):
      if not (root.start <= index <= root.end):
        return root.max
      root.max = value
      if root.start == index == root.end:
        return root.max
      root.max = max(recurse(root.left), recurse(root.right))
      return root.max

    recurse(root)

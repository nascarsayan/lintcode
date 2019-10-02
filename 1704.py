"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
  """
  @param root: the root node
  @param L: an integer
  @param R: an integer
  @return: the sum
  """

  def rangeSumBST(self, root, L, R):
    # write your code here.
    def recurse(root):
      if root is None:
        return 0
      v = 0
      if L <= root.val <= R:
        v += root.val
      if root.val > L:
        v += recurse(root.left)
      if root.val < R:
        v += recurse(root.right)
      return v

    return recurse(root)

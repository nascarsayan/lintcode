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
  @param root: the root
  @return: the maximum width of the given tree
  """

  def widthOfBinaryTree(self, root):
    # Write your code here
    def recurse(root, v, dep):
      if root is None:
        return
      if dep == len(minv):
        minv.append(v)
      mw[0] = max(mw[0], v - minv[dep] + 1)
      recurse(root.left, v * 2, dep + 1)
      recurse(root.right, v * 2 + 1, dep + 1)

    minv = []
    if root is None:
      return 0
    mw = [0]
    recurse(root, 0, 0)
    return mw[0]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
  @param root: a TreeNode
  @return: return a boolean
  """

  def checkEqualTree(self, root):
    # write your code here
    def settot(root):
      if root is None:
        return 0
      root.tot = settot(root.left) + settot(root.right) + root.val
      return root.tot

    def brkpnt(root):
      if root is None:
        return False
      if root.tot == v[0]:
        return True
      return any(brkpnt(node) for node in [root.left, root.right])

    settot(root)
    if root is None or root.tot % 2 == 1:
      return False
    v = [root.tot // 2]
    if brkpnt(root.left):
      return True
    return brkpnt(root.right)

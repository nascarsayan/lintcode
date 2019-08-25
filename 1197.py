"""
Definition of TreeNode:
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
"""


class Solution:
  """
  @param root: a root of tree
  @return: return a integer
  """

  def findBottomLeftValue(self, root):
    # write your code here
    def recurse(root, lv):
      if root is None:
        return
      recurse(root.left, lv + 1)
      if lv > lm[0]:
        lm[0] = lv
        lm[1] = root.val
      recurse(root.right, lv + 1)

    lm = [-1, None]
    recurse(root, 0)
    return lm[1]

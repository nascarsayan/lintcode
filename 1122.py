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
  @param root: the root of binary tree
  @param v: a integer
  @param d: a integer
  @return: return a TreeNode
  """

  def addOneRow(self, root, v, d):
    # write your code here
    def recurse(root, curdep):
      if root is None:
        return
      if curdep == d - 1:
        nlt = TreeNode(v)
        nrt = TreeNode(v)
        root.left, nlt.left = nlt, root.left
        root.right, nrt.right = nrt, root.right
        return
      recurse(root.left, curdep + 1)
      recurse(root.right, curdep + 1)

    if d == 1:
      nr = TreeNode(v)
      nr.left = root
      return nr
    recurse(root, 1)
    return root

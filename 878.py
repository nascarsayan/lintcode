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
  @return: a list of integer
  """

  def boundaryOfBinaryTree(self, root):
    # write your code here
    circum = []

    def prleft(root):
      if root is None or (root.left is None and root.right is None):
        return
      circum.append(root.val)
      if root.left is not None:
        prleft(root.left)
      else:
        prleft(root.right)

    def prleaf(root):
      if root is None:
        return
      if root.left is None and root.right is None:
        circum.append(root.val)
      prleaf(root.left)
      prleaf(root.right)

    def prright(root):
      if root is None or (root.left is None and root.right is None):
        return
      if root.right is not None:
        prright(root.right)
      else:
        prright(root.left)
      circum.append(root.val)

    if root is None:
      return circum
    circum.append(root.val)
    prleft(root.left)
    prleaf(root.left)
    prleaf(root.right)
    prright(root.right)
    return circum

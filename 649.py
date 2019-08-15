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
  @return: new root
  """

  def upsideDownBinaryTree(self, root):
    # write your code here
    if root is None or root.left is None:
      return root

    def recurse(oroot, nroot):
      if oroot.left is None:
        return nroot
      nnode = TreeNode(oroot.left.val)
      nnode.left = oroot.right
      nnode.right = nroot
      return recurse(oroot.left, nnode)

    nroot = TreeNode(root.val)
    return recurse(root, nroot)

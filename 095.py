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
  @param root: The root of binary tree.
  @return: True if the binary tree is BST, or false
  """

  def recurse(self, root, alpha, beta):
    if root is None:
      return True
    if not (root.val > alpha and root.val < beta):
      return False
    return (self.recurse(root.left, alpha, root.val) and
            self.recurse(root.right, root.val, beta))

  def isValidBST(self, root):
    # write your code here
    return self.recurse(root, float('-inf'), float('inf'))

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
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

  def buildTree(self, inorder, postorder):
    # write your code here
    size = len(inorder)
    if size == 0:
      return None
    rootval = postorder.pop(-1)
    root = TreeNode(rootval)
    idx = inorder.index(rootval)
    root.right = self.buildTree(inorder[idx + 1:], postorder)
    root.left = self.buildTree(inorder[:idx], postorder)
    return root

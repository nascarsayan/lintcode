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

  def recurse(self, preorder, inorder):
    lin = len(inorder)
    if lin == 0:
      return None
    rootval = preorder.pop(0)
    root = TreeNode(rootval)
    rootidx = inorder.index(rootval)
    root.left = self.recurse(preorder, inorder[:rootidx])
    root.right = self.recurse(preorder, inorder[rootidx + 1:])
    return root

  """
  @param preorder : A list of integers that preorder traversal of a tree
  @param inorder : A list of integers that inorder traversal of a tree
  @return : Root of a tree
  """

  def buildTree(self, preorder, inorder):
    # write your code here
    if len(preorder) == 0:
      return None
    if len(preorder) != len(inorder):
      return None
    return self.recurse(preorder, inorder)

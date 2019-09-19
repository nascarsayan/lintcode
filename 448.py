"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
  """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

  def inorderSuccessor(self, root, p):
    # write your code here
    if p is None or root is None:
      return None
    if p.right is not None:
      node = p.right
      while node.left is not None:
        node = node.left
      return node
    if root == p:
      return None
    curr = root
    desc = None
    while (curr and curr != p):
      if p.val > curr.val:
        curr = curr.right
      else:
        desc = curr
        curr = curr.left
    return desc

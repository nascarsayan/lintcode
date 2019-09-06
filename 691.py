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
  @param root: the given tree
  @return: the tree after swapping
  """

  def bstSwappedNode(self, root):
    # write your code here
    def recurse(root):
      if root is None:
        return
      recurse(root.left)
      if root.val < prev[0].val:
        invs.append([prev[0], root])
      prev[0] = root
      recurse(root.right)

    invs = []
    prev = [TreeNode(float('-inf'))]
    recurse(root)
    if len(invs) == 0:
      return root
    if len(invs) == 1:
      invs[0][0].val, invs[0][1].val = invs[0][1].val, invs[0][0].val
    else:
      mx = max([invs[0][0], invs[1][0]], key=lambda x: x.val)
      mn = min([invs[0][1], invs[1][1]], key=lambda x: x.val)
      mx.val, mn.val = mn.val, mx.val
    return root

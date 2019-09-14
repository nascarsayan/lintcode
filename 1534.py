"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
  @param root: root of a tree
  @return: head node of a doubly linked list
  """

  def treeToDoublyList(self, root):
    # Write your code here.
    def recurse(root):
      if root is None:
        return (None, None)
      st, fl = root, root
      if root.left is not None:
        lst, lfl = recurse(root.left)
        lfl.right = root
        root.left = lfl
        st = lst
      if root.right is not None:
        rst, rfl = recurse(root.right)
        root.right = rst
        rst.left = root
        fl = rfl
      return (st, fl)

    if root is None:
      return None
    hd, tl = recurse(root)
    hd.left = tl
    tl.right = hd
    return hd

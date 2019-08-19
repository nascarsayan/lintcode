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
  @param root: the root of the tree
  @return: the total sum of all root-to-leaf numbers
  """

  def sumNumbers(self, root):
    # write your code here
    def recurse(root, path):
      if root is None:
        return
      elif root.left is None and root.right is None:
        tot[0] += int(path + str(root.val))
      else:
        recurse(root.left, path + str(root.val))
        recurse(root.right, path + str(root.val))

    path = ''
    tot = [0]
    recurse(root, path)
    return tot[0]

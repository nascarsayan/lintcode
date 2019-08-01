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

  def recurse(self, root, level, trav):
    if root is None:
      return
    size = len(trav)
    if level == size:
      trav.append([])
    if level % 2 == 0:
      trav[level].append(root.val)
    else:
      trav[level].insert(0, root.val)
    self.recurse(root.left, level + 1, trav)
    self.recurse(root.right, level + 1, trav)

  """
  @param root: A Tree
  @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
  """

  def zigzagLevelOrder(self, root):
    # write your code here
    trav = []
    self.recurse(root, 0, trav)
    return trav

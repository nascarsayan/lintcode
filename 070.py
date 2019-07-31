from collections import defaultdict
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

  def recurse(self, root, level, maxlev, lvl2node):
    if root is None:
      return
    if maxlev[0] < level:
      maxlev[0] = level
    lvl2node[level].append(root.val)
    self.recurse(root.left, level + 1, maxlev, lvl2node)
    self.recurse(root.right, level + 1, maxlev, lvl2node)

  """
  @param root: A tree
  @return: buttom-up level order a list of lists of integer
  """

  def levelOrderBottom(self, root):
    # write your code here
    lvl2node = defaultdict(list)
    maxlev = [0]
    lotrav = []
    self.recurse(root, 0, maxlev, lvl2node)
    if len(lvl2node.keys()) > 0:
      for level in range(maxlev[0], -1, -1):
        lotrav.append(lvl2node[level])
    return lotrav

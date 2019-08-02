from collections import defaultdict
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

  def rightSideView(self, root):
    # write your code here
    if not root:
      return []
    trav = defaultdict(int)

    def recurse(root, level):
      if not root:
        return
      trav[level] = root.val
      recurse(root.left, level + 1)
      recurse(root.right, level + 1)

    recurse(root, 0)
    keys = trav.keys()
    mxdep = max(keys)
    return [trav[k] for k in range(mxdep + 1)]

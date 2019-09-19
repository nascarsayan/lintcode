"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """

  def countUnivalSubtrees(self, root):
    # write your code here
    tot = [0]

    def dfs(root):
      if root is None:
        return None
      if all(x is None for x in [root.left, root.right]):
        tot[0] += 1
        return root.val
      lv = rv = root.val
      if root.left:
        lv = dfs(root.left)
      if root.right:
        rv = dfs(root.right)
      if lv == rv == root.val:
        tot[0] += 1
        return root.val
      return None

    dfs(root)
    return tot[0]

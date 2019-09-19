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
    @return: Whether it is a full tree
    """

  def isFullTree(self, root):
    # write your code here
    def dfs(root):
      if all(x is None for x in [root.left, root.right]):
        return True
      if any(x is None for x in [root.left, root.right]):
        return False
      return dfs(root.left) and dfs(root.right)

    if root is None:
      return True
    return dfs(root)

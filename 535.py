"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """

  def recurse(self, root):
    if not root:
      return [0, 0]
    [l1, l2] = self.recurse(root.left)
    [r1, r2] = self.recurse(root.right)
    return [root.val + l2 + r2, max(l1 + r1, l1 + r2, l2 + r1, l2 + r2)]

  def houseRobber3(self, root):
    # write your code here
    if not root:
      return 0
    return max(self.recurse(root))

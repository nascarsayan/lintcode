"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """

  def pathSum(self, root, gsum):
    # Write your code here.
    def recurse(root, path, csum):
      csum += root.val
      if root.left is not None:
        recurse(root.left, path + [root.val], csum)
      if root.right is not None:
        recurse(root.right, path + [root.val], csum)
      if all(x is None for x in [root.left, root.right]) and csum == gsum:
        allp.append(path + [root.val])

    allp = []
    recurse(root, [], 0)
    return allp

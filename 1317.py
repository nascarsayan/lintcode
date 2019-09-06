"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
  @param root: root of complete binary tree
  @return: the number of nodes
  """

  def countNodes(self, root):
    # write your code here
    cnt = [0]

    def recurse(root):
      if root is None:
        return
      cnt[0] += 1
      recurse(root.left)
      recurse(root.right)

    recurse(root)
    return cnt[0]

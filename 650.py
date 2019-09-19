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
  @param: root: the root of binary tree
  @return: collect and remove all leaves
  """

  def findLeaves(self, root):
    # write your code here
    resdi, res = defaultdict(list), []

    def recurse(root):
      if root is None:
        return -1
      dep = max(recurse(root.left), recurse(root.right)) + 1
      resdi[dep].append(root.val)
      return dep

    recurse(root)
    for dep in sorted(resdi.keys()):
      res.append(resdi[dep])
    return res

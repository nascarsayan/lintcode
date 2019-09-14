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
  @param root: a root of integer
  @return: return a list of integer
  """

  def largestValues(self, root):
    # write your code here
    def recurse(root, depth):
      if root is None:
        return
      mx[depth] = max(mx[depth], root.val)
      recurse(root.left, depth + 1)
      recurse(root.right, depth + 1)

    ninf = float('-inf')
    mx = defaultdict(lambda: ninf)
    recurse(root, 0)
    mxv, lev = [], 0
    while (True):
      if mx[lev] == ninf:
        break
      mxv.append(mx[lev])
      lev += 1
    return mxv

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
  """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """

  def findFrequentTreeSum(self, root):
    # Write your code here
    ninf = float('-inf')
    mx = [ninf]

    def recurse(root):
      if root is None:
        return ninf
      s = root.val
      sl, sr = recurse(root.left), recurse(root.right)
      for v in [sl, sr]:
        if v > ninf:
          s += v
      s2f[s] += 1
      f2s[s2f[s]].append(s)
      mx[0] = max(mx[0], s2f[s])
      return s

    s2f, f2s = defaultdict(int), defaultdict(list)
    recurse(root)
    return f2s[mx[0]]

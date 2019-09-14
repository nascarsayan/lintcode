from collections import Counter
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
  @return: return a integer list
  """

  def findMode(self, root):
    # write your code here
    def recurse(root):
      if root is None:
        return
      cnt[root.val] += 1
      recurse(root.left)
      recurse(root.right)

    if root is None:
      return None
    cnt = Counter()
    recurse(root)
    mc = list(cnt.most_common())
    if mc[0][1] == mc[-1][1]:
      return [el for el, v in mc]
    mode, idx = [], 0
    while (mc[idx][1] == mc[0][1]):
      mode.append(mc[idx][0])
      idx += 1
    return mode

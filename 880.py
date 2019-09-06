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
    @param s: a string
    @return: a root of this tree
    """

  def str2tree(self, s):
    # write your code here
    size = len(s)
    if size == '':
      return None
    lp = s.find('(')
    if lp == -1:
      return TreeNode(int(s))
    root = TreeNode(int(s[:lp]))
    rp, cnt = lp + 1, 1
    while (cnt > 0):
      if s[rp] == ')':
        cnt -= 1
      elif s[rp] == '(':
        cnt += 1
      rp += 1
    rp -= 1
    root.left = self.str2tree(s[lp + 1:rp])
    if rp < size - 1:
      root.right = self.str2tree(s[rp + 2:-1])
    return root

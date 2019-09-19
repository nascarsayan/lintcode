"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
  @param root: the root of binary tree
  @return: the length of the longest consecutive sequence path
  """

  def longestConsecutive2(self, root):
    # write your code here
    inf = float('inf')

    def recurse(root, par=inf):
      if root is None:
        return ((-1, inf, inf), (-1, inf, inf))
      linc, ldec = recurse(root.left, root.val)
      rinc, rdec = recurse(root.right, root.val)
      for dec, inc in [(ldec, rinc), (rdec, linc)]:
        if dec[0] != -1 and inc[0] != -1:
          mxi[0] = max(mxi[0], (inc[2] - dec[2], dec[2], inc[2]))
      inc, dec = (0, root.val, root.val), (0, root.val, root.val)
      for span, st, fl in [linc, rinc]:
        if span != -1:
          inc = max(inc, (span + 1, root.val, fl))
          mxi[0] = max(mxi[0], inc)
      for span, fl, st in [ldec, rdec]:
        if span != -1:
          dec = max(dec, (span + 1, root.val, st))
          mxi[0] = max(mxi[0], dec)
      if root.val != par + 1:
        inc = (-1, inf, inf)
      if root.val != par - 1:
        dec = (-1, inf, inf)
      return (inc, dec)

    if root is None:
      return []
    mxi = [(0, root.val, root.val)]
    recurse(root)
    return mxi[0][0] + 1

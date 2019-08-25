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
  @return: the binary tree in an m*n 2D string array
  """

  def printTree(self, root):
    # Write your code here
    def getMaxdep(root, currd):
      if root is None:
        maxd[0] = max(maxd[0], currd)
        return
      getMaxdep(root.left, currd + 1)
      getMaxdep(root.right, currd + 1)

    def fill(root, st, fl, currd):
      if root is None:
        return
      mid = (st + fl) >> 1
      li[currd][mid] = str(root.val)
      fill(root.left, st, mid - 1, currd + 1)
      fill(root.right, mid + 1, fl, currd + 1)

    if root is None:
      return []
    maxd = [0]
    getMaxdep(root, 0)
    li = [[''] * int(pow(2, maxd[0]) - 1) for _ in range(maxd[0])]
    fill(root, 0, len(li[0]) - 1, 0)
    return li

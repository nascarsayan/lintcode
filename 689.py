"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
  @param: : the root of tree
  @param: : the target sum
  @return: two numbers from tree which sum is n
  """

  def twoSum(self, root, n):
    # write your code here
    inov = []

    def ino(root):
      if root is None:
        return
      ino(root.left)
      inov.append(root.val)
      ino(root.right)

    ino(root)
    st, fl = 0, len(inov) - 1
    while (st < fl):
      curr = inov[st] + inov[fl]
      if curr == n:
        return [inov[st], inov[fl]]
      if curr < n:
        st += 1
      else:
        fl -= 1
    return None

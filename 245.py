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
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """

  def isSubtree(self, T1, T2):
    # write your code here
    def recurse(r1, r2):
      if r1 is None and r2 is None:
        return True
      if r1 is None:
        return False
      if r2 is not None:
        if (r1.val == r2.val):
          if (recurse(r1.left, r2.left) and recurse(r1.right, r2.right)):
            return True
      if id(r2) != id(T2):
        if (r1.val == T2.val):
          return (recurse(r1.left, T2.left) and recurse(r1.right, T2.right))
      return recurse(r1.left, r2) or recurse(r1.right, r2)

    if T2 is None:
      return True
    return recurse(T1, T2)


# T1 = TreeNode(1)
# T2 = TreeNode(2)
# T3 = TreeNode(3)
# T4 = TreeNode(4)
# T1.left = T2
# T1.right = T3
# T3.left = T4

# T5 = TreeNode(3)
# T6 = TreeNode(4)
# T5.left = T6
# print(Solution().isSubtree(T1, T5))

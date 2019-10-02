from Serial import BTSerial
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

  def constructFromPrePost(self, pre, post):
    # write your code here
    ptr = [0]

    def recurse(rem):
      if ptr[0] >= len(pre) or not rem:
        return None
      try:
        posti = rem.index(pre[ptr[0]])
      except ValueError:
        return None
      root = TreeNode(pre[ptr[0]])
      ptr[0] += 1
      root.left = recurse(rem[:posti])
      root.right = recurse(rem[:posti])
      return root

    return recurse(post)


print(BTSerial().serialize(Solution().constructFromPrePost([1, 2, 3, 4],
                                                           [3, 2, 4, 1])))

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

  def recurse(self, nums):
    size = len(nums)
    if size == 0:
      return [None]
    roots = []
    for idx, num in enumerate(nums):
      lefts = self.recurse(nums[:idx])
      rights = self.recurse(nums[idx + 1:])
      for left in lefts:
        for right in rights:
          root = TreeNode(num)
          root.left = left
          root.right = right
          roots.append(root)
    return roots

  # @paramn n: An integer
  # @return: A list of root
  def generateTrees(self, n):
    # write your code here
    return self.recurse(list(range(1, n + 1)))

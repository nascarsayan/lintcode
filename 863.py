class MyTreeNode:

  def __init__(self, dig3):
    self.val = dig3 % 10
    self.dep = dig3 // 100
    self.pos = (dig3 // 10) % 10
    self.left, self.right = None, None


class Solution:
  """
  @param nums: a list of integers
  @return: return an integer
  """

  def pathSum(self, nums):
    # write your code here
    def recurse(root, node):
      if (node.dep == root.dep + 1):
        if node.pos % 2 == 1:
          root.left = node
        else:
          root.right = node
      else:
        nsubl = int(pow(2, node.dep - root.dep - 1))
        if node.pos - (root.pos - 1) * 2 * nsubl <= nsubl:
          recurse(root.left, node)
        else:
          recurse(root.right, node)

    def getsum(root, path):
      if root is None:
        return
      path += root.val
      if all(x is None for x in [root.left, root.right]):
        tot[0] += path
      else:
        getsum(root.left, path)
        getsum(root.right, path)

    tot = 0
    if len(nums) == 0:
      return tot
    root = MyTreeNode(nums[0])
    for num in nums[1:]:
      node = MyTreeNode(num)
      recurse(root, node)
    tot = [0]
    getsum(root, 0)
    return tot[0]


print(Solution().pathSum([113, 215, 221]))

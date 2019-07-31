# https://www.lintcode.com/problem/permutations/


class Solution:

  def __init__(self):
    self.perm = []

  def helper(self, nums, k):
    if k == 1:
      self.perm.append(nums[:])
      return
    self.helper(nums, k - 1)
    for i in range(k - 1):
      if k % 2 == 0:
        nums[i], nums[k - 1] = nums[k - 1], nums[i]
      else:
        nums[0], nums[k - 1] = nums[k - 1], nums[0]
      self.helper(nums, k - 1)

  """
  @param: nums: A list of integers.
  @return: A list of permutations.
  """

  def permute(self, nums):
    # write your code here
    size = len(nums)
    if (size == 0):
      return [[]]
    if size == 1:
      return [nums]
    self.helper(nums, size)
    return self.perm


# print(Solution().permute([1, 2, 3, 4]))

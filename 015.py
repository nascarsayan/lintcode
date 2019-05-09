# https://www.lintcode.com/problem/permutations/

class Solution:

  def __init__(self):
    self.perm = []
  
  def helper(self, nums, start):
    if (start == len(nums) - 1):
      self.perm.append(nums[:])
      return
    for tarpos in range(start, len(nums)):
      nums[start], nums[tarpos] = nums[tarpos], nums[start]
      self.helper(nums, start + 1)
      nums[start], nums[tarpos] = nums[tarpos], nums[start]

  """
  @param: nums: A list of integers.
  @return: A list of permutations.
  """
  def permute(self, nums):
    # write your code here
    if (len(nums) == 0):
      return [[]]
    self.helper(nums, 0)
    return self.perm

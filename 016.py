# https://www.lintcode.com/problem/permutations-ii/

class Solution:

  def __init__(self):
    self.perm = []
  
  def helper(self, nums, start):
    if (start == len(nums) - 1):
      self.perm.append(nums[:])
      return
    for tarpos in range(start, len(nums)):
      if (nums[tarpos] in nums[start:tarpos]):
        continue
      nums[start], nums[tarpos] = nums[tarpos], nums[start]
      self.helper(nums, start + 1)
      nums[start], nums[tarpos] = nums[tarpos], nums[start]
  
  """
  @param: :  A list of integers
  @return: A list of unique permutations
  """

  def permuteUnique(self, nums):
    # write your code here
    if (len(nums) == 0):
      return [[]]
    self.helper(nums, 0)
    return self.perm
  
# print(Solution().permuteUnique([1, 2, 2]))
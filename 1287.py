class Solution:
  """
  @param nums: a list of integers
  @return: return a boolean
  """

  def increasingTriplet(self, nums):
    # write your code
    size = len(nums)
    mid = None
    for i in range(size - 1):
      if nums[i] < nums[i + 1]:
        if mid is None:
          mid = nums[i + 1]
        else:
          if mid < nums[i + 1]:
            return True
          mid = nums[i + 1]
    return False


print(Solution().increasingTriplet([1, 2, 1, 0, 1, 2]))

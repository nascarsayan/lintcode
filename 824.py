class Solution:
  """
  @param nums: The number array
  @return: Return the single number
  """

  def getSingleNumber(self, nums):
    # Write your code here
    size = len(nums)
    st, fl = 0, size - 1
    while (st < fl):
      mid = (st + fl) >> 1
      if mid == 0 or mid == size - 1:
        return nums[mid]
      if nums[mid] == nums[mid + 1]:
        if mid % 2 == 1:
          fl = mid - 1
        else:
          st = mid + 2
      elif nums[mid] == nums[mid - 1]:
        if (mid - 1) % 2 == 1:
          fl = mid - 2
        else:
          st = mid + 1
      else:
        return nums[mid]
    return nums[st]


print(Solution().getSingleNumber([1]))

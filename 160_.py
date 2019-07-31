class Solution:
  """
  @param nums: a rotated sorted array
  @return: the minimum number in the array
  """

  def findMin(self, nums):
    # write your code here
    size = len(nums)
    if size == 0:
      return None
    if nums[0] <= nums[-1]:
      return nums[0]
    st = 0
    fl = size - 2
    while (st <= fl):
      mid = (st + fl) // 2
      if nums[mid] > nums[mid + 1]:
        return nums[mid + 1]
      if nums[st] > nums[st + 1]:
        return nums[st + 1]
      if nums[fl] > nums[fl + 1]:
        return nums[fl + 1]
      if nums[mid] < nums[fl]:
        fl = mid
      else:
        st = mid + 1
    return None

class Solution:
  """
    @param nums: a list of integers
    @return: return a integer
    """

  def singleNonDuplicate(self, nums):
    # write your code here
    size = len(nums)
    if size == 0:
      return None
    st, fl = 0, size - 1
    while (st < fl):
      mid = (st + fl) // 2
      if nums[mid - 1] != nums[mid] != nums[mid + 1]:
        return nums[mid]
      if nums[mid] == nums[mid + 1]:
        mid1, mid2 = mid - 1, mid + 2
      else:
        mid1, mid2 = mid - 2, mid + 1
      if (mid1 - st) % 2 == 0:
        fl = mid1
      else:
        st = mid2
    return nums[st]


print(Solution().singleNonDuplicate([1, 1, 2]))

import bisect


class Solution:
  """
    @param nums: An array of integers
    @return: nothing
    """

  def nextPermutation(self, nums):
    # write your code here
    size = len(nums)
    if size < 2:
      return nums
    i = size - 1
    while (i > 0 and nums[i - 1] >= nums[i]):
      i -= 1
    if i == 0:
      nums.reverse()
    else:
      idx = bisect.bisect_right(list(reversed(nums[i:])), nums[i - 1])
      nums[i - 1], nums[size - 1 - idx] = nums[size - 1 - idx], nums[i - 1]
      st, fl = i, size - 1
      while (st < fl):
        nums[st], nums[fl] = nums[fl], nums[st]
        st, fl = st + 1, fl - 1
    return nums


print(Solution().nextPermutation([2, 4, 3, 3, 1]))

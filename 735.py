import bisect


class Solution:
  """
  @param nums: An array of integers.
  @return: nothing
  """

  def arrayReplaceWithGreatestFromRight(self, nums):
    # Write your code here.
    size = len(nums)
    res = [None] * size
    if size == 0:
      return
    res[-1], arr = -1, [nums[-1]]
    for idx in range(size - 1)[::-1]:
      res[idx] = arr[-1]
      pos = bisect.bisect_left(arr, nums[idx])
      arr.insert(pos, nums[idx])
    for idx in range(size):
      nums[idx] = res[idx]


print(Solution().arrayReplaceWithGreatestFromRight([16, 17, 4, 3, 5, 2]))

import math


class Solution:
  """
  @param nums: an array of integers
  @return: the maximun difference
  """

  def maximumGap(self, nums):
    # write your code here
    size = len(nums)
    if size < 2:
      return 0
    mxi, ci = int(math.log10(max(nums))), 0
    while (ci <= mxi):
      nex = [0] * size
      bucket = [0] * 10
      for num in nums:
        bucket[(num // 10**ci) % 10] += 1
      for i in range(1, 10):
        bucket[i] += bucket[i - 1]
      for num in nums[::-1]:
        idx = (num // 10**ci) % 10
        bucket[idx] -= 1
        nex[bucket[idx]] = num
      nums = nex
      ci += 1
    mxg = 0
    for i in range(1, size):
      mxg = max(mxg, nums[i] - nums[i - 1])
    return mxg


print(Solution().maximumGap([11, 9, 202, 51]))

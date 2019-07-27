class Solution:
  """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

  def minSubArray(self, nums):
    # write your code here
    l = len(nums)
    ninf = float('-inf')
    for idx in range(l):
      nums[idx] = -nums[idx]
    csum = 0
    msum = ninf
    for idx in range(l):
      csum += nums[idx]
      if csum > msum:
        msum = csum
      if csum < 0:
        csum = 0
    return -msum


# print(Solution().minSubArray([1, -1, -2, 1, -4]))
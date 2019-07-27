class Solution:
  """
  @param nums: A list of integers
  @return: A integer indicate the sum of max subarray
  """

  def maxSubArray(self, nums):
    # write your code here
    ms = float('-inf')
    s = 0
    for num in nums:
      s += num
      if (s > ms):
        ms = s
      if s < 0:
        s = 0
    return ms

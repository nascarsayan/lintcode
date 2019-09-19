class Solution:
  """
  @param nums: an array with positive and negative numbers
  @param k: an integer
  @return: the maximum average
  """

  def maxAverage(self, nums, k):
    # write your code here
    if k == 0:
      return None
    size = len(nums)
    s0k = sum(nums[:k])

    def hasgt(mid):
      curr = (s0k - mid * k)
      if curr >= 0:
        return True
      pre, mnpre = 0, 0
      for i in range(k, size):
        pre += nums[i - k] - mid
        mnpre = min(mnpre, pre)
        curr += nums[i] - mid
        if curr - mnpre >= 0:
          return True
      return False

    hi, lo = max(nums), min(nums)
    while (hi - lo > 1e-6):
      mid = (hi + lo) / 2
      if hasgt(mid):
        lo = mid
      else:
        hi = mid
    return hi


print(Solution().maxAverage([1, 12, -5, -6, 50, 3], 3))

# !TLE
# def maxAverage(self, nums, k):
#   # write your code here
#   if k == 0:
#     return None
#   size = len(nums)
#   dp = [[0] * i for i in range(1, size - k + 2)[::-1]]
#   dp[0][0] = sum(nums[:k]) / k
#   for i in range(1, size - k + 1):
#     dp[0][i] = (dp[0][i - 1] * k + nums[i + k - 1] - nums[i - 1]) / k
#   for span in range(1, len(dp)):
#     dp[span][0] = (dp[span - 1][0] * (k + span - 1) + nums[span + k - 1]) / (
#         k + span)
#     for i in range(1, len(dp[span])):
#       dp[span][i] = (dp[span][i - 1] *
#                       (k + span) + nums[i + k + span - 1] - nums[i - 1]) / (
#                           k + span)
#   mx = float('-inf')
#   for ir in range(len(dp)):
#     for ic in range(len(dp[ir])):
#       mx = max(mx, dp[ir][ic])
#   return mx

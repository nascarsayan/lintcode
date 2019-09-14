from collections import Counter


class Solution:
  """
  @param nums: the given array
  @param s: the given target
  @return: the number of ways to assign symbols to make sum of integers equal to target S
  """

  def findTargetSumWays(self, nums, s):
    # Write your code here
    if len(nums) == 0:
      return 0
    dp = Counter([nums[0], -nums[0]])
    for num in nums[1:]:
      dp2 = Counter()
      for k in dp.keys():
        dp2[k + num] += dp[k]
        dp2[k - num] += dp[k]
      dp = dp2
    return dp[s]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

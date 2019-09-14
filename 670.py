# from collections import defaultdict


class Solution:
  """
  @param nums: nums an array of scores
  @return: check if player 1 will win
  """

  def PredictTheWinner(self, nums):
    # write your code here
    size = len(nums)
    # dp = defaultdict(int)
    dp = [[0] * sz for sz in range(1, size + 1)[::-1]]
    for st in range(size):
      dp[st][0] = nums[st]
    for sp in range(1, size):
      for st in range(size - sp):
        dp[st][sp] = max(nums[st] - dp[st + 1][sp - 1],
                         nums[st + sp] - dp[st][sp - 1])
    return dp[0][size - 1] >= 0

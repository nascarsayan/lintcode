class Solution:
  """
  @param prices: the prices
  @param n: the length of rod
  @return: the max value
  """

  def cutting(self, prices, n):
    # Write your code here
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
      dp[i] = max([dp[i - j - 1] + prices[j] for j in range(i)])
    return dp[-1]


print(Solution().cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))

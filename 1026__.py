class Solution:
  """
  @param N: a integer
  @return: return a integer
  """

  def numTilings(self, N):
    # write your code here
    pr = 1000000007
    dp = [1, 1, 2, 5]
    if N < 4:
      return dp[N]
    for i in range(4, N + 1):
      dp = [dp[1], dp[2], dp[3], dp[-1] + dp[-2] + 2 * (dp[-3] + dp[-4])]
    return dp[-1] % pr


print(Solution().numTilings(5))

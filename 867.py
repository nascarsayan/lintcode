class Solution:
  """
  @param N: an integer
  @return: return an integer
  """

  def maxA(self, N):
    # write your code here
    if N < 4:
      return N
    dp = list(range(N + 1))
    for n in range(4, N + 1):
      dp[n] = max(dp[n - 1] + 1,
                  max([dp[i] * (n - i - 1) for i in range(n - 2)]))
    return dp[N]


print(Solution().maxA(10))

class Solution:
  """
  @param n: The number of 'A'
  @return: the minimum number of steps to get n 'A'
  """

  def minSteps(self, n):
    # Write your code here
    dp = list(range(n + 1))
    dp[1] = 0
    for i in range(2, n + 1):
      mxfac = int(i // 2)
      for fac in range(1, mxfac + 1):
        if i % fac == 0:
          dp[i] = min(dp[i], dp[fac] + i // fac)
    return dp[-1]


print(Solution().minSteps(36))

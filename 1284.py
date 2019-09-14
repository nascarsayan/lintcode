class Solution:
  """
  @param n: a positive integer n
  @return: the maximum product you can get
  """

  def integerBreak(self, n):
    # Write your code here
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
      for j in range(1, i):
        dp[i] = max([
            dp[i], dp[j] * dp[i - j], dp[j] * (i - j), j * dp[i - j],
            j * (i - j)
        ])
    print(dp)
    return dp[n]


print(Solution().integerBreak(15))

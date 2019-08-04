class Solution:
  """
    @param n: An integer
    @return: An integer
    """

  def numTrees(self, n):
    # write your code here
    dp = [0] * (n + 1)
    dp[0] = 1
    for idx in range(1, n + 1):
      for mid in range(idx):
        dp[idx] += dp[mid] * dp[idx - mid - 1]
    return dp[n]


# print(Solution().numTrees(5))

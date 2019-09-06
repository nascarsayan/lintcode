class Solution:
  """
  @param n: a positive integer
  @return: the minimum number of replacements
  """

  def integerReplacement(self, n):
    # Write your code here
    def recurse(n):
      if n in dp:
        return dp[n]
      if n % 2 == 0:
        dp[n] = recurse(n // 2) + 1
      else:
        dp[n] = min(recurse(n - 1), recurse(n + 1)) + 1
      return dp[n]

    dp = {1: 0}
    recurse(n)
    return dp[n]

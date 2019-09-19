class Solution:
  """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

  def fastPower(self, a, b, n):
    # write your code here
    if b == 1:
      return 0
    dp = {}

    def fp(n):
      if n == 0:
        return 1
      if n == 1:
        return a % b
      if n in dp:
        return dp[n]
      dp[n] = (fp(n >> 1) * fp(n - (n >> 1))) % b
      return dp[n]

    return fp(n)


print(Solution().fastPower(3, 7, 5))

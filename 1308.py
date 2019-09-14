class Solution:
  """
  @param n: a integer
  @return: return a 2D array
  """

  def getFactors(self, n):
    # write your code here
    dp = {}

    def facs(n):
      if n in dp:
        return dp[n]
      res = []
      for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
          res.append([i, n // i])
          subs = facs(n // i)
          for sub in subs:
            if sub[0] >= i:
              res.append([i] + sub)
      dp[n] = res
      return dp[n]

    return facs(n)


print(Solution().getFactors(16))

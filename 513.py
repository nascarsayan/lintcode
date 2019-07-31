import math


class Solution:
  """
  @param n: a positive integer
  @return: An integer
  """

  def numSquares(self, n):
    # write your code here
    dp = [None] * n
    dp[0] = 1
    pers = [1]
    for i in range(2, n + 1):
      near = int(math.sqrt(i))
      nearsq = near * near
      if nearsq == i:
        pers.append(i)
        dp[i - 1] = 1
        continue
      least = float('inf')
      for num in range(1, near + 1):
        least = min(least, dp[i - num * num - 1])
      dp[i - 1] = least + 1
    return dp[n - 1]


# print(Solution().numSquares(13))

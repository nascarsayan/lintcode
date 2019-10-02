class Solution:
  """
    @param N: an integer
    @return: return any beautiful array A
    """

  def beautifulArray(self, N):
    # write your code here.
    dp = [None] * (N + 1)
    dp[1] = [1]
    for i in range(2, N + 1):
      dp[i] = ([2 * x - 1 for x in dp[(i + 1) // 2]] +
               [2 * x for x in dp[i // 2]])
    return dp[N]


print(Solution().beautifulArray(10))

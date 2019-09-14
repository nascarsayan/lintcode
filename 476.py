class Solution:
  """
  @param A: An integer array
  @return: An integer
  """

  def stoneGame(self, A):
    # write your code here
    size = len(A)
    if size < 2:
      return 0
    szdp = [0]
    for i in range(size):
      szdp.append(szdp[-1] + A[i])
    # szdp.pop(0)
    dp = [[float('inf')] * size for _ in range(size)]
    for i in range(size):
      dp[i][i] = 0
    for sp in range(1, size):
      for i in range(size - sp):
        for mid in range(sp):
          dp[i][i + sp] = min(
              dp[i][i + sp], dp[i][i + mid] + dp[i + mid + 1][i + sp] +
              szdp[i + sp + 1] - szdp[i])
    return dp[0][size - 1]


print(Solution().stoneGame([3, 4]))

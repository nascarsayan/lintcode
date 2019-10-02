class Solution:
  """
  @param: A: An integer array
  @param: target: An integer
  @return: An integer
  """

  def MinAdjustmentCost(self, A, target):
    # write your code here
    mx, size, inf = max(A), len(A), float('inf')
    nr, nc = size + 1, mx + 1
    dp = [[inf] * nc for _ in range(nr)]
    for ic in range(nc):
      dp[0][ic] = 0
    for ir in range(1, nr):
      for ic in range(nc):
        dp[ir][ic] = min(
            dp[ir - 1][max(0, ic - target):min(nc - 1, ic + target) +
                       1]) + abs(A[ir - 1] - ic)
    return min(dp[-1])


print(Solution().MinAdjustmentCost([3, 5, 4, 7], 2))

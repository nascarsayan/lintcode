class Solution:
  """
  @param N: size of 2D grid
  @param mines: in the given list
  @return: the order of the plus sign
  """

  def orderOfLargestPlusSign(self, N, mines):
    # Write your code here
    dp = [[[1] * 4 for _ in range(N)] for _ in range(N)]
    for ir, ic in mines:
      dp[ir][ic] = [0] * 4
    for i1 in range(1, N):
      for i2 in range(1, N):
        idcs = [[i1, i2], [N - i1 - 1, i2], [i2, i1], [N - i2 - 1, N - i1 - 1]]
        dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for idx in range(4):
          ir, ic = idcs[idx]
          dr, dc = dxy[idx]
          if dp[ir][ic][0] == 0:
            continue
          dp[ir][ic][idx] += dp[ir + dr][ic + dc][idx]
    mxv = 0
    for ir in range(N):
      for ic in range(N):
        mxv = max(mxv, min(dp[ir][ic]))
    return mxv


print(Solution().orderOfLargestPlusSign(1000, []))

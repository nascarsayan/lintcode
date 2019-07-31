class Solution:
  """
  @param A: A list of integers
  @return: An integer
  """

  def jump(self, A):
    # write your code here
    size = len(A)
    if size < 2:
      return 0
    inf = float('inf')
    dp = [inf] * size
    dp[-1] = 0
    for idx in range(size - 2, -1, -1):
      if A[idx] >= size - 1 - idx:
        dp[idx] = 1
        continue
      minjmp = inf
      for nex in range(idx + 1, min(size - 1, idx + A[idx] + 1)):
        minjmp = min(minjmp, dp[nex] + 1)
      dp[idx] = minjmp
    return dp[0]


# print(Solution().jump([2, 3, 1, 1, 4]))

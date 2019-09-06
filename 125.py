class Solution:
  """
  @param m: An integer m denotes the size of a backpack
  @param A: Given n items with size A[i]
  @param V: Given n items with value V[i]
  @return: The maximum value
  """

  def backPackII(self, m, A, V):
    # write your code here
    nr, nc = len(A) + 1, (m + 1)
    dp = [0] * nc
    for ir in range(1, nr):
      dp2 = dp[:]
      for ic in range(A[ir - 1], nc):
        dp2[ic] = max(dp[ic], dp[ic - A[ir - 1]] + V[ir - 1])
      dp = dp2
    return dp[-1]


print(Solution().backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4]))

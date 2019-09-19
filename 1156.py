class Solution:
  """
  @param word1: a string
  @param word2: a string
  @return: return a integer
  """

  def minDistance(self, word1, word2):
    # write your code here
    nr, nc = len(word1) + 1, len(word2) + 1
    dp = [[float('inf')] * nc for _ in range(nr)]
    for ir in range(nr):
      dp[ir][0] = ir
    for ic in range(nc):
      dp[0][ic] = ic
    for ir in range(1, nr):
      for ic in range(1, nc):
        dp[ir][ic] = min(dp[ir - 1][ic], dp[ir][ic - 1]) + 1
        if word1[ir - 1] == word2[ic - 1]:
          dp[ir][ic] = min(dp[ir][ic], dp[ir - 1][ic - 1])
    return dp[-1][-1]


print(Solution().minDistance('ros', 'horse'))

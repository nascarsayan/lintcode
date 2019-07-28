class Solution:
  """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

  def minDistance(self, word1, word2):
    # write your code here
    size1 = len(word1)
    size2 = len(word2)
    dp = [[None] * (size1 + 1) for _ in range(size2 + 1)]
    for j in range(size1 + 1):
      dp[0][j] = j
    for i in range(size2 + 1):
      dp[i][0] = i
    for i in range(1, size2 + 1):
      for j in range(1, size1 + 1):
        repcost = dp[i - 1][j - 1]
        if word1[j - 1] == word2[i - 1]:
          repcost -= 1
        dp[i][j] = min([repcost, dp[i - 1][j], dp[i][j - 1]]) + 1
    return dp[size2][size1]


# print(Solution().minDistance('horse', 'ros'))

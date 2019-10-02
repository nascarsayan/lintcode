class Solution:
  """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """

  def minimumDeleteSum(self, s1, s2):
    # Write your code here
    nr, nc = len(s1) + 1, len(s2) + 1
    dp = [[0] * nc for ir in range(nr)]
    for ir in range(1, nr):
      dp[ir][0] = dp[ir - 1][0] + ord(s1[ir - 1])
    for ic in range(1, nc):
      dp[0][ic] = dp[0][ic - 1] + ord(s2[ic - 1])
    for ir in range(1, nr):
      for ic in range(1, nc):
        if s1[ir - 1] == s2[ic - 1]:
          dp[ir][ic] = dp[ir - 1][ic - 1]
        else:
          dp[ir][ic] = min(dp[ir][ic - 1] + ord(s2[ic - 1]),
                           dp[ir - 1][ic] + ord(s1[ir - 1]))
    return dp[-1][-1]


print(Solution().minimumDeleteSum('sea', 'eat'))

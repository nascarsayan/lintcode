from collections import Counter


class Solution:
  """
  @param strs: an array with strings include only 0 and 1
  @param m: An integer
  @param n: An integer
  @return: find the maximum number of strings
  """

  def findMaxForm(self, strs, m, n):
    # write your code here
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for zo in strs:
      cnt = Counter(zo)
      for ir in range(cnt['1'], n + 1)[::-1]:
        for ic in range(cnt['0'], m + 1)[::-1]:
          dp[ir][ic] = max(dp[ir][ic], dp[ir - cnt['1']][ic - cnt['0']] + 1)
    return dp[n][m]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))

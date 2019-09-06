from collections import defaultdict


class Solution:
  """
  @param A: an array
  @param K: an integer
  @return: the largest score
  """

  def largestSumOfAverages(self, A, K):
    # Write your code here
    tot = defaultdict(int)
    dp = defaultdict(float)
    size = len(A)
    for i, a in enumerate(A):
      tot[i] = tot[i - 1] + a
      dp[(0, i)] = tot[i] / (i + 1)
    for k in range(1, K):
      for i in range(k, size):
        for j in range(k - 1, i):
          dp[(k, i)] = max(dp[(k, i)],
                           dp[(k - 1, j)] + (tot[i] - tot[j]) / (i - j))
    return dp[(K - 1, size - 1)]


print(Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3))

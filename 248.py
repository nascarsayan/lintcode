class Solution:
  """
  @param A: An integer array
  @param queries: The query list
  @return: The number of element in the array that are smaller that the given integer
  """

  def countOfSmallerNumber(self, A, queries):
    # write your code here
    size = len(A)
    if size == 0:
      return [0] * len(queries)
    mx = max(A)
    dp = [0] * (mx + 1)
    for num in A:
      dp[num] += 1
    for i in range(1, mx + 1):
      dp[i] += dp[i - 1]
    res = []
    for fl in queries:
      if fl == 0:
        res.append(0)
      else:
        res.append(dp[min(fl - 1, mx)])
    return res

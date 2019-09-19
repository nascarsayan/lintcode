from collections import defaultdict


class Solution:
  """
  @param A:
  @return: nothing
  """

  def numFactoredBinaryTrees(self, A):
    #
    nums = set(A)
    A = list(nums)
    dp = {}

    def recurse(root):
      if root in dp:
        return dp[root]
      res = 1
      for x, y in fac[root]:
        res += recurse(x) * recurse(y)
      dp[root] = res
      return dp[root]

    res = 0
    fac = defaultdict(list)
    for xy in A:
      for x in A:
        if xy % x == 0 and (xy // x) in nums:
          fac[xy].append((x, xy // x))

    for a in A:
      res += recurse(a)
    # print(dp)
    return res


print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))

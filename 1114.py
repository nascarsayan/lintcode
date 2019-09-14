# from collections import defaultdict


class Solution:
  """
  @param price: List[int]
  @param special: List[List[int]]
  @param needs: List[int]
  @return: return an integer
  """

  # !Heavy Top Down
  def shoppingOffers(self, price, special, needs):
    # write your code here
    dp = {}
    inf = float('inf')

    def recurse(needs):
      if any(x < 0 for x in needs):
        return inf
      tneed = tuple(needs)
      if tneed in dp:
        return dp[tneed]
      mn = sum(list(map(lambda x: x[0] * x[1], zip(needs, price))))
      for sp in special:
        left = list(map(lambda x: x[0] - x[1], zip(needs, sp[:-1])))
        mn = min(mn, recurse(left) + sp[-1])
      dp[tneed] = mn
      return dp[tneed]

    recurse(needs)
    return dp[tuple(needs)]

  # !TODO Light Bottom Up
  # def shoppingOffers(self, price, special, needs):
  #   # write your code here
  #   inf = float('inf')

  #   class mydict(defaultdict):

  #     def __init__(self, fx):
  #       super().__init__(None)
  #       self.fn = fn

  #     def __missing__(self, x):
  #       self[x] = self.fn(x)
  #       return self[x]

  #   def fn(needs):
  #     if any(xi < 0 for xi in needs):
  #       return inf
  #     return sum(map(lambda x: x[0] * x[1], zip(needs, price)))

  #   size = len(needs)
  #   if size == 0:
  #     return 0
  #   dp = mydict(fn)
  #   for ir in range(len(needs)):
  #     for ic in range(needs[ir] + 1):
  #       cneed = needs[:ir] + [ic] + [0] * (len(needs) - 1 - ir)
  #       tneed = tuple(cneed)
  #       for sp in special:
  #         left = list(map(lambda x: x[0] - x[1], zip(cneed, sp[:-1])))
  #         dp[tneed] = min(dp[tneed], sp[-1] + dp[tuple(left)])
  #   print(dp)
  #   return dp[tuple(needs)]


print(Solution().shoppingOffers([9, 9], [[1, 1, 1]], [2, 2]))

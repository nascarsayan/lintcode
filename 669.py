from collections import defaultdict


class Solution:
  """
  @param coins: a list of integer
  @param amount: a total amount of money amount
  @return: the fewest number of coins that you need to make up
  """

  def coinChange(self, coins, amount):
    # write your code here
    if amount == 0:
      return 0
    coins.sort()
    nc = len(coins)
    inf = float('inf')
    dp = defaultdict(lambda: inf)
    for ic in range(nc):
      dp[(0, ic)] = 0
    for ir in range(1, amount + 1):
      for ic in range(nc):
        dp[(ir, ic)] = min(dp[(ir, ic - 1)], dp[(ir - coins[ic], ic)] + 1)
    if dp[(amount, nc - 1)] == inf:
      return -1
    return dp[(amount, nc - 1)]


print(Solution().coinChange([1, 2, 5], 11))

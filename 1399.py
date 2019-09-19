class Solution:
  """
  @param coins: The coins
  @param k: The k
  @return: The answer
  """

  def takeCoins(self, coins, k):
    # Write your code here
    tot = sum(coins)
    size = len(coins)
    nk = size - k
    curr = 0
    for i in range(nk):
      curr += coins[i]
    mn = curr
    for i in range(size - nk):
      curr += coins[i + nk] - coins[i]
      mn = min(mn, curr)
    return tot - mn


print(Solution().takeCoins([5, 4, 3, 2, 1], 2))

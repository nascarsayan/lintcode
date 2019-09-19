class Solution:
  """
  @param amount: a total amount of money amount
  @param coins: the denomination of each coin
  @return: the number of combinations that make up the amount
  """

  def change(self, amount, coins):
    # write your code here
    if amount == 0:
      return 1
    dp = [0] * (amount + 1)
    for coin in coins:
      if coin <= amount:
        dp[coin] += 1
      for i in range(coin + 1, amount + 1):
        dp[i] += dp[i - coin]
    return dp[amount]


print(Solution().change(8, [2, 3, 8]))

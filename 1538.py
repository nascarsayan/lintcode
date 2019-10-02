class Solution:
  """
  @param cost: costs of all cards
  @param damage: damage of all cards
  @param totalMoney: total of money
  @param totalDamage: the damage you need to inflict
  @return: Determine if you can win the game
  """

  def cardGame(self, cost, damage, totalMoney, totalDamage):
    # Write your code here
    dp = [0] * (totalMoney + 1)
    for ir in range(len(cost)):
      for ic in range(cost[ir], totalMoney + 1)[::-1]:
        dp[ic] = max(dp[ic], dp[ic - cost[ir]] + damage[ir])
      if dp[-1] >= totalDamage:
        return True
    return dp[-1] >= totalDamage


print(Solution().cardGame([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10, 10))

# !TLE dp maxDamage X cards
# * OK dp totalMoney X cards
# def cardGame(self, cost, damage, totalMoney, totalDamage):
#   # Write your code here
#   dp = [float('inf')] * (totalDamage + 1)
#   dp[0] = 0
#   for ir in range(len(damage)):
#     for ic in range(min(damage[ir], totalDamage + 1)):
#       dp[ic] = min(dp[ic], cost[ir])
#     for ic in range(damage[ir], totalDamage + 1)[::-1]:
#       dp[ic] = min(dp[ic], dp[ic - damage[ir]] + cost[ir])
#   return dp[-1] <= totalMoney

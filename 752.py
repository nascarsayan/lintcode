# from collections import defaultdict
# import heapq


class Solution:
  """
  @param n: the max identifier of planet.
  @param m: gold coins that Sven has.
  @param limit: the max difference.
  @param cost: the number of gold coins that reaching the planet j through the portal costs.
  @return: return the number of ways he can reach the planet n through the portal.
  """

  def getNumberOfWays(self, n, m, limit, cost):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0] = [1] * (m + 1)
    for i in range(1, n + 1):
      for j in range(cost[i], m + 1):
        for k in range(max(0, i - limit), i):
          dp[i][j] += dp[k][j - cost[i]]
    return dp[n][m]


print(Solution().getNumberOfWays(5, 8, 13, [0, 1, 2, 3, 2, 1]))

# !Solution using Merge K sorted arrays using Heap
# def getNumberOfWays(self, n, m, limit, cost):
#   if n == 0:
#     return 0
#   costs = defaultdict(list)
#   costs[0].append(0)
#   for i in range(1, n + 1):
#     hop1 = []
#     for j in range(max(0, i - limit), i):
#       heapq.heappush(hop1, (costs[j][0], (j, 0)))
#     while (len(hop1) > 0 and hop1[0][0] + cost[i] <= m):
#       costk, (k, ik) = heapq.heappop(hop1)
#       costs[i].append(costk + cost[i])
#       if ik < len(costs[k]) - 1:
#         heapq.heappush(hop1, (costs[k][ik + 1], (k, ik + 1)))
#   return len(costs[n])

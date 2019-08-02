class Solution:
  """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

  def minCost(self, costs):
    # write your code here
    n = len(costs)
    if n == 0:
      return 0
    for idx in range(1, n):
      costs[idx][0] += min(costs[idx - 1][1:])
      costs[idx][1] += min(costs[idx - 1][::2])
      costs[idx][2] += min(costs[idx - 1][:-1])
    return min(costs[-1])

class Solution:
  """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

  def maxProfit(self, K, prices):
    # write your code here
    size = len(prices)
    if size < 2:
      return 0
    if K >= size >> 1:
      total = 0
      for idx in range(1, size):
        total += max(prices[idx] - prices[idx - 1], 0)
      return total
    ninf = float('-inf')
    dp = [ninf] * size
    buy = [ninf] * K
    sell = [0] * K
    buy[0] = -prices[0]
    for idx in range(1, size):
      buy[0] = max(buy[0], -prices[idx])
      sell[0] = max(sell[0], prices[idx] + buy[0])
      for trans in range(1, K):
        buy[trans] = max(buy[trans], sell[trans - 1] - prices[idx])
        sell[trans] = max(sell[trans], buy[trans] + prices[idx])
      dp[idx] = sell[K - 1]
    return max(sell[K - 1], 0)


# print(Solution().maxProfit(2, [4, 4, 6, 1, 1, 4, 2, 5]))

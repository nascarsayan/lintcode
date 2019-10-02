class Solution:
  """
  @param prices: a list of integers
  @return: return a integer
  """

  def maxProfit(self, prices):
    # write your code here
    size = len(prices)
    buy = [0] * size
    sell = [0] * size
    if size < 1:
      return 0
    buy[0] = -prices[0]
    if size > 1:
      buy[1] = max(buy[0], sell[0] - prices[1])
      sell[1] = max(sell[0], buy[0] + prices[1])
    for i in range(2, size):
      buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
      sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
    return sell[-1]


print(Solution().maxProfit([3, 2, 6, 5, 0, 3]))

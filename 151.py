class Solution:
  """
    @param prices: Given an integer array
    @return: Maximum profit
    """

  def maxProfit(self, prices):
    # write your code here
    size = len(prices)
    if size < 2:
      return 0
    ltr = [0] * size
    rtl = [0] * size
    minltr = prices[0]
    for idx in range(1, size):
      ltr[idx] = max(ltr[idx], prices[idx] - minltr, ltr[idx - 1])
      minltr = min(minltr, prices[idx])
    maxrtl = prices[-1]
    for idx in range(size - 2, -1, -1):
      rtl[idx] = max(rtl[idx], maxrtl - prices[idx], rtl[idx + 1])
      maxrtl = max(maxrtl, prices[idx])
    maxP = ltr[-1]
    for idx in range(1, size - 2):
      maxP = max(maxP, ltr[idx] + rtl[idx + 1])
    return maxP


# print(Solution().maxProfit([4, 4, 6, 1, 1, 4, 2, 5]))

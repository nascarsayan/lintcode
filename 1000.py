class Solution:
  """
  @param prices: a list of integers
  @param fee: a integer
  @return: return a integer
  """

  def maxProfit(self, prices, fee):
    # write your code here
    present, absent = -prices[0], 0  # Stock is present in or absent from hand
    for i in range(1, len(prices)):
      present, absent = max(present,
                            absent - prices[i]), max(absent,
                                                     present + prices[i] - fee)
    return absent


print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))

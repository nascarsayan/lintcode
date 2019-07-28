class Solution:
  """
    @param prices: Given an integer array
    @return: Maximum profit
    """

  def maxProfit(self, prices):
    # write your code here
    today = 0
    boughtOn = None
    days = len(prices)
    profit = 0
    for today in range(days):
      if (boughtOn is None and today < days - 1 and
          prices[today + 1] > prices[today]):
        boughtOn = today
        profit -= prices[today]
      elif (boughtOn is not None and
            (today == days - 1 or prices[today + 1] < prices[today])):
        profit += prices[today]
        boughtOn = None
    return profit


# print(Solution().maxProfit([2, 1, 2, 0, 1]))

class Solution:
  """
    @param prices: Given an integer array
    @return: Maximum profit
    """

  def maxProfit(self, prices):
    # write your code here
    ndays = len(prices)
    if ndays < 2:
      return 0
    maxrtl = [None] * ndays
    minltr = [None] * ndays
    maxrtl[ndays - 1] = prices[-1]
    minltr[0] = prices[0]
    maxP = 0
    for idx in range(ndays - 2, -1, -1):
      maxrtl[idx] = max(maxrtl[idx + 1], prices[idx])
    for idx in range(1, ndays):
      minltr[idx] = min(minltr[idx - 1], prices[idx])
    for idx in range(ndays):
      maxP = max(maxP, maxrtl[idx] - minltr[idx])
    return maxP


print(Solution().maxProfit([2, 1, 4, 5, 2, 9, 7]))
'''
Basic version
'''
# # Unlimited transactions total, at most 1 buy, sell 1 daay
# class Solution:
#   """
#     @param prices: Given an integer array
#     @return: Maximum profit
#     """

#   def maxProfit(self, prices):
#     # write your code here
#     today = 0
#     boughtOn = None
#     days = len(prices)
#     profit = 0
#     maxP = 0
#     for today in range(days):
#       if (boughtOn is None and today < days - 1 and
#           prices[today + 1] > prices[today]):
#         boughtOn = today
#         profit -= prices[today]
#       elif (boughtOn is not None and
#             (today == days - 1 or prices[today + 1] < prices[today])):
#         profit += prices[today]
#         maxP = max(profit, maxP)
#         profit = 0
#         boughtOn = None
#     return maxP

# # print(Solution().maxProfit([3, 2, 3, 1, 2]))

# import math


class Solution:
  """
  @param num: a non negative integer number
  @return: an array represent the number of 1's in their binary
  """

  def countBits(self, num):
    # write your code here
    dp = [None] * (num + 1)
    dp[0] = 0
    if num == 0:
      return dp
    dp[1] = 1
    for i in range(2, num + 1):
      dp[i] = dp[i >> 1] + i % 2
    return dp


print(Solution().countBits(5))

# !Program to count the total number of 1's from 0 -> n
# def countBits(self, num):
#   # write your code here
#   if num == 0:
#     return 0
#   msb = int(math.log2(num))
#   tot = 0
#   for pos in range(msb + 1):
#     div = 2**(pos + 1)
#     tot += ((num + 1) // div) * (pos + 1)
#     tot += max(0, num - (((num + 1) // div) * div + 2**pos) + 1)
#     print(tot)
#   return tot

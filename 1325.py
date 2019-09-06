import math


class Solution:
  """
  @param m: an Integer
  @param n: an Integer
  @return: the bitwise AND of all numbers in [m,n]
  """

  def rangeBitwiseAnd(self, m, n):
    # Write your code here
    if m == 0 or n == 0:
      return 0
    mxp = int(math.log2(m))
    aand = 0
    for i in range(mxp + 1):
      p2 = 1 << i
      if (m & p2 and n & p2 and n - m < p2):
        aand += p2
    return aand


print(Solution().rangeBitwiseAnd(5, 7))

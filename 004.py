# https://www.lintcode.com/problem/ugly-number-ii/

import heapq


class Solution:
  """
  @param n: An integer
  @return: return a  integer as description.
  """

  def nthUglyNumber(self, n):
    # write your code here
    facs = [2, 3, 5]
    if n == 1:
      return 1
    hp = facs[:]
    nth = None
    for i in range(1, n):
      nth = heapq.heappop(hp)
      for fac in facs:
        if nth * fac not in hp:
          heapq.heappush(hp, nth * fac)
    return nth


print(Solution().nthUglyNumber(9))

import math


class Solution:
  """
  @param piles: an array
  @param H: an integer
  @return: the minimum integer K
  """

  def minEatingSpeed(self, piles, H):
    # Write your code here
    st, fl = 1, max(piles)
    opti = fl
    while (st <= fl):
      mid = (st + fl) // 2
      currt = sum(list(map(lambda x: math.ceil(x / mid), piles)))
      if currt > H:
        st = mid + 1
      else:
        opti = min(opti, mid)
        fl = mid - 1
    return opti


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))

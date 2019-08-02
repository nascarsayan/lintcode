# https://www.lintcode.com/problem/ugly-number-ii/
# TODO : subete
class Solution:
  """
  @param n: An integer
  @return: return a  integer as description.
  """

  def nthUglyNumber(self, n):
    # write your code here
    if (n < 1):
      return None
    if (n == 1):
      return 1
    f = {2: 2, 3: 3, 5: 5}
    ptr = 2
    for idx in range(3, n + 1):
      if ptr == 2:
        f[2] += 2
        if f[2] > f[3]:
          ptr = 3
      elif ptr == 3:
        f[3] += 3
        if f[3] > f[5]:
          ptr = 5
        else:
          ptr = 2
      else:
        f[5] += 5
        ptr = 2
      print(f[ptr])
    return f[ptr]


print(Solution().nthUglyNumber(9))

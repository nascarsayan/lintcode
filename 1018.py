from collections import defaultdict


class Solution:
  """
  @param poured: an integer
  @param query_row: an integer
  @param query_glass: an integer
  @return: return a double
  """

  def champagneTower(self, poured, query_row, query_glass):
    # write your code here
    pyra = defaultdict(int)
    pyra[0] = poured
    for ir in range(1, query_row + 1):
      for ic in range(ir, -1, -1):
        t = max((pyra[ic] - 1) / 2, 0)
        pyra[ic + 1] += t
        pyra[ic] = t
    return min(pyra[query_glass] + 0.0, 1.0)


print(Solution().champagneTower(6, 2, 0))
# def champagneTower(self, poured, query_row, query_glass):
#   # write your code here
#   def gcd(n1, n2):
#     while (n1 > 0):
#       n1, n2 = n2 % n1, n1
#     return n2

#   def ncr(n, r):
#     if n == 0:
#       return 1
#     if n - r < r:
#       r = n - r
#     num, den = 1, 1
#     while (r > 0):
#       num *= n
#       den *= r
#       g = gcd(num, den)
#       num //= g
#       den //= g
#       n -= 1
#       r -= 1
#     return num

#   def sumofnat(n):
#     return (n * (n + 1)) // 2

#   leftover = poured - sumofnat((query_row))
#   if leftover <= 0:
#     return 0
#   if poured >= sumofnat((query_row + 1)):
#     return 1
#   return leftover * (ncr(query_row, query_glass)) / pow(2, query_row)

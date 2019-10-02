class Solution:
  """
  @param n: an array consisting of n integers from 1 to n
  @return: the number of derangement it can generate
  """

  def findDerangement(self, n):
    # Write your code here
    if n < 2:
      return 0
    res, PR = 0, 10**9 + 7
    coef = 1 if n % 2 == 0 else -1
    fac, prod = n, 1
    while (fac >= 2):
      res = (res + coef * prod) % PR
      prod = (prod * fac) % PR
      fac -= 1
      coef *= -1
    return res


print(Solution().findDerangement(4))

class Solution:
  """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """

  def isThreeDisctFactors(self, n):
    # write your code here
    sqrtn = int(n**0.5)
    if sqrtn**2 != n:
      return False
    for i in range(2, int(sqrtn**0.5) + 1):
      if sqrtn % i == 0:
        return False
    return True


print(Solution().isThreeDisctFactors(10000))

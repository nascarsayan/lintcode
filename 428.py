class Solution:

  def recurse(self, x, n, pows):
    if n == 0:
      pows[n] = 1
      return pows[n]
    if n == 1:
      pows[n] = x
      return pows[n]
    if n == -1:
      pows[n] = 1 / x
      return pows[n]
    if n in pows:
      return pows[n]
    pows[n] = self.recurse(x, n // 2, pows) * self.recurse(x, n - n // 2, pows)
    return pows[n]

  """
  @param x {float}: the base number
  @param n {int}: the power number
  @return {float}: the result
  """

  def myPow(self, x, n):
    # write your code here
    pows = {}
    return self.recurse(x, n, pows)

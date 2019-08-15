class Solution:
  """
    @param n: an integer
    @return: return a string
    """

  def lastFourDigitsOfFn(self, n):
    # write your code here
    n %= 15000
    f = [0, 1]
    if n == 0:
      return '0'
    for i in range(2, n % 15000 + 1):
      f = [f[1] % 10000, (f[0] + f[1]) % 10000]
    return '%04d' % f[1]


print(Solution().lastFourDigitsOfFn(5531354))

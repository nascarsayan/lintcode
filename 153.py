class Solution:
  """
    @param n: An integer
    @return: return a  integer as description.
    """

  def nthUglyNumber(self, n):
    # write your code here
    f = {2: 2, 3: 3, 5: 5}
    if (n < 1):
      return -1
    if (n == 1):
      return f[2]
    if (n == 2):
      return f[3]
    if (n == 3):
      return f[5]
    cnt = 3
    while (True):
      ptr = None
      if f[2] <= f[3]:
        f[2] += 2
        ptr = 2
      # elif f[2] > f[3]

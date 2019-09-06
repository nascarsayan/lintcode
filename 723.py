class Solution:
  """
    @param n: a number
    @param d: digit needed to be rorated
    @return: a number
    """

  def leftRotate(self, n, d):
    # write code here
    sn = '{:032b}'.format(n)
    d %= 32
    sn = sn[d:] + sn[:d]
    return int(sn, 2)

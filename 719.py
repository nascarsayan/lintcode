from functools import reduce


class Solution:
  """
  @param str: the given string
  @return: the maximum value
  """

  def calcMaxValue(self, digs):
    # write your code here
    size = len(digs)
    if size == 0:
      return 0
    digs = list(map(int, digs))
    return reduce(lambda x, y: max(y * x, x + y), digs)


print(Solution().calcMaxValue('891'))

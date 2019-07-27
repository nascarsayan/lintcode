# https://www.lintcode.com/problem/gray-code/description


class Solution:
  """
    @param n: a number
    @return: Gray code
    """

  def grayCode(self, n):
    # write your code here
    nseq = int(pow(2, n))
    seq = []
    for row in range(nseq):
      v = 0
      for col in range(n):
        div = int(pow(2, col))
        dig = (row // div + (row // (2 * div))) % 2
        v += dig << col
      seq.append(v)
    return seq


# print(Solution().grayCode(3))
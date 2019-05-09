# https://www.lintcode.com/problem/trailing-zeros/
class Solution:
  """
  @param: n: An integer
  @return: An integer, denote the number of trailing zeros in n!
  """
  def trailingZeros(self, n):
    # write your code here, try to do it without arithmetic operators.
    tot = 0
    DIV = 5
    curr = DIV
    while(n >= curr):
      tot += n // curr
      curr *= DIV
    return tot

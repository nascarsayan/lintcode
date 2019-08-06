"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Point:

  def __init__(self, a=0, b=0):
    self.x = a
    self.y = b


class Solution:
  """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
  def numIslands2(self, n, m, operators):
    # write your code here
    isls = []
    osize = len(operators)
    if n == 0 or m == 0:
      return [0] * osize
    numisl = []
    for operator in operators:
      coag = []
      xo = operator.x
      yo = operator.y
      dif = 0
      for i, isl in enumerate(isls):
        if any((x, y) in isl for (x, y) in [(xo, yo - 1), (xo - 1, yo), (xo, yo + 1), (xo + 1, yo), (xo, yo)]):
          coag.append(i - dif)
          dif += 1
      newisl = set()
      for i in coag:
        newisl = newisl.union(isls[i])
        isls.pop(i)
      newisl.add((xo, yo))
      isls.append(newisl)
      numisl.append(len(isls))
    return numisl


p = []
p.append(Point(0, 0))
p.append(Point(1, 1))
p.append(Point(1, 0))
p.append(Point(0, 1))

print(Solution().numIslands2(2, 2, p))

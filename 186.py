from collections import defaultdict
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

# class Point:

#   def __init__(self, a=0, b=0):
#     self.x = a
#     self.y = b


class Solution:
  """
    @param points: an array of point
    @return: An integer
    """

  def gcd(self, x, y):
    if x == 0:
      return y
    if y == 0:
      return x
    while (x != 0):
      x, y = y % x, x
    return y

  def maxPoints(self, points):
    # write your code here
    if len(points) == 0:
      return 0
    if len(points) == 1:
      return 1
    size = len(points)
    maxp = 1
    for one in range(size - 1):
      over = 0
      ver = 0
      slopecnt = defaultdict(int)
      for two in range(one + 1, size):
        p1 = points[one]
        p2 = points[two]
        if p1.x == p2.x:
          if p1.y == p2.y:
            over += 1
          else:
            ver += 1
        else:
          my = p2.y - p1.y
          mx = p2.x - p1.x
          factor = self.gcd(my, mx)
          my, mx = my // factor, mx // factor
          if my * mx < 0:
            my = -abs(my)
            mx = abs(mx)
          slopecnt[(my, mx)] += 1
      maxp = max(maxp, ver + over + 1)
      for v in slopecnt.values():
        maxp = max(maxp, v + over + 1)
    return maxp


# print(Solution().maxPoints([
#     Point(-4, -4),
#     Point(-8, -582),
#     Point(-3, 3),
#     Point(-9, -651),
#     Point(9, 591),
# ]))

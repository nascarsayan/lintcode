class Solution:
  """
  @param points: a list of two-tuples
  @return: a boolean, denote whether the polygon is convex
  """

  def isConvex(self, points):
    # write your code here
    def orient(p1, p2, p3):
      return (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (
          p3[0] - p2[0])

    size = len(points)
    if size < 3:
      return False
    cori = 0
    for i in range(size):
      nori = orient(points[i], points[(i + 1) % size], points[(i + 2) % size])
      if cori == 0 and nori != 0:
        cori = nori
      if cori * nori < 0:
        return False
    return cori != 0

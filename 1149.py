class Solution:
  """
  @param p1: the first point
  @param p2: the second point
  @param p3: the third point
  @param p4: the fourth point
  @return: whether the four points could construct a square
  """

  def validSquare(self, p1, p2, p3, p4):
    # Write your code here
    def euclid(p1, p2):
      return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

    for pp1, pp2, pp3, pp4 in [(p1, p2, p3, p4), (p1, p2, p4, p3),
                               (p1, p3, p2, p4), (p1, p3, p4, p2),
                               (p1, p4, p2, p3), (p1, p4, p3, p2)]:
      side = euclid(pp1, pp2)
      if all(
          euclid(px, py) == side
          for px, py in [(pp2, pp3), (pp3, pp4), (pp4, pp1)]) and euclid(
              pp1, pp3) == euclid(pp2, pp4):
        return True
    return False

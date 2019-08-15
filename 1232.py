class Solution:
  """
    @param points: a 2D array
    @return: the minimum number of arrows that must be shot to burst all balloons
    """

  def findMinArrowShots(self, points):
    # Write your code here
    points.sort(key=lambda x: x[0])
    stac = []
    for point in points:
      if len(stac) == 0 or stac[-1][1] < point[0]:
        stac.append(point)
      else:
        stac[-1] = [max(stac[-1][0], point[0]), min(stac[-1][1], point[1])]
    return len(stac)

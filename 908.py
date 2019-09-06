from collections import defaultdict


class Solution:
  """
  @param points: n points on a 2D plane
  @return: if there is such a line parallel to y-axis that reflect the given points
  """

  def isReflected(self, points):
    # Write your code here
    size = len(points)
    if size == 1:
      return True
    hori = defaultdict(list)
    for x, y in points:
      hori[y].append(x)
    hori[y].sort()
    mid = hori[y][0] + (hori[y][-1] - hori[y][0]) / 2
    for y in hori.keys():
      arr = hori[y]
      arr.sort()
      size = len(arr)
      for i in range((size + 1) // 2):
        if abs((arr[i] + (arr[-i - 1] - arr[i]) / 2) - mid) > 0.25:
          return False
    return True

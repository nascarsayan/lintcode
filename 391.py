"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
  """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

  def countOfAirplanes(self, airplanes):
    # write your code here
    invs = []
    for inv in airplanes:
      invs.append((inv.start, 1))
      invs.append((inv.end, -1))
    mx, curr = 0, 0
    for _, dif in sorted(invs):
      curr += dif
      mx = max(mx, curr)
    return mx

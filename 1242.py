"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
  """
  @param intervals: a collection of intervals
  @return: the minimum number of intervals you need to remove
  """

  def eraseOverlapIntervals(self, intervals):
    # write your code here
    intervals.sort(key=lambda x: (x.start, x.end))
    end = float('inf')
    rem = 0
    for inv in intervals:
      st, fl = inv.start, inv.end
      if st < end:
        rem += 1
        end = min(end, fl)
      else:
        end = fl
    return max(0, rem - 1)

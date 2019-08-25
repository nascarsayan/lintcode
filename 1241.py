"""
Definition of Interval.
class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
"""


class Solution:
  """
  @param intervals: a list of intervals
  @return: return a list of integers
  """

  def findRightInterval(self, intervals):
    # write your code here
    size = len(intervals)
    stint = sorted(range(size), key=lambda x: intervals[x].start)
    flint = sorted(range(size), key=lambda x: intervals[x].end)
    rtint = [-1] * size
    sti, fli = 0, 0
    while (sti < size and fli < size):
      while (sti < size and
             intervals[stint[sti]].start < intervals[flint[fli]].end):
        sti += 1
      if sti < size:
        rtint[flint[fli]] = stint[sti]
      fli += 1
    return rtint

# https://www.lintcode.com/problem/insert-interval/description
"""
Definition of Interval.

"""

# class Interval(object):

#   def __init__(self, start, end):
#     self.start = start
#     self.end = end

#   def __repr__(self):
#     return "(%d, %d)" % (self.start, self.end)


class Solution:
  """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """

  def merge(self, intervals):
    st = 1
    while (st < len(intervals)):
      if (intervals[st - 1].end >= intervals[st].start):
        intervals[st] = Interval(
            min(intervals[st].start, intervals[st - 1].start),
            max(intervals[st].end, intervals[st - 1].end))
        del intervals[st - 1]
        if (st > 1):
          st -= 1
      else:
        st += 1

  def insert(self, intervals, newInterval):
    # write your code here
    l = len(intervals)
    st = 0
    fl = l - 1
    idx = None
    while (st <= fl and (idx == None)):
      mid = (st + fl) // 2
      if (st == fl):
        if (intervals[st].start >= newInterval.start):
          idx = mid
        else:
          idx = mid + 1
        break
      if (intervals[mid].start >= newInterval.start and
          (mid == 0 or intervals[mid - 1].start <= newInterval.start)):
        idx = mid
      elif (mid > 0 and intervals[mid - 1].start >= newInterval.start):
        fl = max(0, mid - 1)
      else:
        st = min(l - 1, mid + 1)
    intervals.insert(idx, newInterval)
    self.merge(intervals)
    return intervals


# print(Solution().insert([Interval(1, 2), Interval(5, 9)], Interval(3, 4)))

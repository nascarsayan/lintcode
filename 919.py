# import heapq
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
  """
  @param intervals: an array of meeting time intervals
  @return: the minimum number of conference rooms required
  """

  # !O(nlgn)
  def minMeetingRooms(self, intervals):
    # Write your code here
    pts, mx, curr = [], 0, 0
    for inv in intervals:
      pts.append((inv.start, 1))
      pts.append((inv.end, -1))
    pts.sort()
    for _, dif in pts:
      curr += dif
      mx = max(mx, curr)
    return mx


# !O(nlgn)

# def minMeetingRooms(self, intervals):
#   # Write your code here
#   size = len(intervals)
#   if size < 2:
#     return size
#   intervals.sort(key=lambda x: (x.start, x.end))
#   hp = []
#   for interval in intervals:
#     st, fl = interval.start, interval.end
#     if len(hp) == 0 or hp[0] > st:
#       heapq.heappush(hp, fl)
#     else:
#       heapq.heapreplace(hp, fl)
#   return len(hp)

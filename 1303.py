import bisect


class Solution:
  """
    @param citations: a list of integers
    @return: return a integer
    """

  def hIndex(self, citations):
    # write your code here
    size = len(citations)
    res = 0
    if size == 0:
      return res
    st, fl = 0, citations[size - 1]
    while (st <= fl):
      mid = (st + fl) // 2
      idx = bisect.bisect_left(citations, mid)
      if (size - idx) >= mid:
        res = mid
        st = mid + 1
      else:
        fl = mid - 1
    return res


print(Solution().hIndex([0, 1, 3, 5, 6]))

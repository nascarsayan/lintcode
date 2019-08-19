import heapq


class Solution:
  """
  @param arr:  an array of non-negative integers
  @return: minimum number of elements
  """

  def minElements(self, arr):
    # write your code here
    tot = sum(arr)
    if tot == 0:
      return len(arr)
    arr2 = list(map(lambda x: (-x, x), arr))
    heapq.heapify(arr2)
    maxs, n = 0, 0
    while (len(arr2) > 0):
      maxs += heapq.heappop(arr2)[1]
      n += 1
      if maxs > (tot - maxs):
        return n
    return n

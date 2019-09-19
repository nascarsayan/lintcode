import heapq


class Solution:
  """
  @param arrays: k sorted integer arrays
  @return: a sorted array
  """

  def mergekSortedArrays(self, arrays):
    # write your code here
    res = []
    hp = []
    for i, array in enumerate(arrays):
      if len(array) > 0:
        heapq.heappush(hp, (array[0], i, 0))
    while (hp):
      val, i, j = heapq.heappop(hp)
      res.append(val)
      if j < len(arrays[i]) - 1:
        heapq.heappush(hp, (arrays[i][j + 1], i, j + 1))
    return res

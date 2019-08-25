import bisect


class Solution:
  """
  @param A: an array
  @return: total of reverse pairs
  """

  def reversePairs(self, A):
    # write your code here
    # if len(A) < 2:
    #   return 0
    stac = []
    tot = 0
    for a in A:
      idx = bisect.bisect_right(stac, a)
      tot += len(stac) - idx
      stac.insert(idx, a)
    return tot


print(Solution().reversePairs([2, 4, 1, 3, 5]))

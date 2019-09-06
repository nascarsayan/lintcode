import bisect


class Solution:
  """
  @param arrs: an array of arrays
  @return: return the max distance among arrays
  """

  def maxDiff(self, arrs):
    # write your code here
    mnh = []
    mxh = []
    for i, arr in enumerate(arrs):
      amn, amx = (arr[0], i), (arr[-1], i)
      idx = bisect.bisect_left(mnh, amn)
      mnh.insert(idx, amn)
      if len(mnh) > 2:
        mnh.pop(-1)
      idx = bisect.bisect_left(mxh, amx)
      mxh.insert(idx, amx)
      if len(mxh) > 2:
        mxh.pop(0)
    if mxh[1][1] != mnh[0][1]:
      return mxh[1][0] - mnh[0][0]
    return max(mxh[0][0] - mnh[0][0], mxh[1][0] - mnh[1][0])


print(Solution().maxDiff([[1, 2, 3], [4, 5], [1, 2, 3]]))

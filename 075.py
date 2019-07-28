class Solution:
  """
    @param A: An integers array.
    @return: return any of peek positions.
    """

  def findPeak(self, A):
    size = len(A)
    lo = 0
    hi = size - 1
    while (lo < hi):
      mid = (hi + lo) >> 1
      if A[mid] < A[mid + 1]:
        lo = mid + 1
      else:
        hi = mid
    return lo

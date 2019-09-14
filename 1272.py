class Solution:
  """
  @param matrix: List[List[int]]
  @param k: a integer
  @return: return a integer
  """

  def kthSmallest(self, matrix, k):
    # write your code here
    nr = len(matrix)
    if nr == 0:
      return None
    nc = len(matrix[0])
    if nc == 0:
      return None

    def lessoreq(mid):
      ir, ic, cnt = 0, nc - 1, 0
      while (ir < nr and ic >= 0):
        if matrix[ir][ic] <= mid:
          cnt += ic + 1
          ir += 1
        else:
          ic -= 1
      return cnt

    st, fl = matrix[0][0], matrix[-1][-1]
    while (st + 1 < fl):
      mid = st + ((fl - st) >> 1)
      if lessoreq(mid) < k:
        st = mid
      else:
        fl = mid
    if lessoreq(st) >= k:
      return st
    return fl

class Solution:
  """
  @param: matrix: an integer matrix
  @return: the coordinate of the left-up and right-down number
  """

  def submatrixSum(self, matrix):
    # write your code here
    try:
      nr, nc = len(matrix), len(matrix[0])
    except Exception:
      return [[-1, -1], [-1, -1]]
    for irtop in range(nr):
      pre = [0] * nc
      for irbtm in range(irtop, nr):
        s2col = {0: -1}
        ctot = 0
        for ic in range(nc):
          pre[ic] += matrix[irbtm][ic]
          ctot += pre[ic]
          if ctot in s2col:
            return [[irtop, s2col[ctot] + 1], [irbtm, ic]]
          s2col[ctot] = ic


print(Solution().submatrixSum([[1, 5, 0]]))

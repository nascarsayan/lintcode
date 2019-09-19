class Solution:
  """
  @param matrix: a 2D array
  @return: return a list of integers
  """

  def findDiagonalOrder(self, matrix):
    # write your code here
    res = []
    nr = len(matrix)
    if nr == 0:
      return res
    nc = len(matrix[0])
    if nc == 0:
      return res
    size = nr + nc - 1
    for idia in range(size):
      ir, ic = idia, 0
      cdia = []
      while (ic <= idia):
        if (0 <= ir < nr and 0 <= ic < nc):
          cdia.append(matrix[ir][ic])
        ir, ic = ir - 1, ic + 1
      if idia % 2 == 1:
        cdia.reverse()
      res.extend(cdia)
    return res


print(Solution().findDiagonalOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                                    [13, 14, 15, 16]]))

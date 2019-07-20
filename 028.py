# https://www.lintcode.com/problem/search-a-2d-matrix/

class Solution:
  """
  @param matrix: matrix, a list of lists of integers
  @param target: An integer
  @return: a boolean, indicate whether matrix contains target
  """
  def searchMatrix(self, matrix, target):
    # write your code here
    try:
      rsize = len(matrix)
      csize = len(matrix[0])
      li = 0
      hi = rsize - 1
      r = None
      while (li <= hi):
        m = (li + hi) // 2
        if (matrix[m][0] <= target and matrix[m][-1] >= target):
          r = m
          break
        if (matrix[m][0] > target):
          hi = m - 1
        elif (matrix[m][-1] < target):
          li = m + 1
      if (r is None):
        return False
      lj = 0
      hj = csize - 1
      while (lj <= hj):
        m = (lj + hj) // 2
        if (matrix[r][m] == target):
          return True
        if (matrix[r][m] > target):
          hj = m - 1
        else:
          lj = m + 1
      return False
    except:
      return False

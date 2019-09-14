class NumMatrix:
  """
  @param: matrix: a 2D matrix
  """

  def __init__(self, matrix):
    # do intialization if necessary
    self.dp = []
    nr = len(matrix)
    if nr == 0:
      self.nr = self.nc = 0
      return
    nc = len(matrix[0])
    if nc == 0:
      self.nr = self.nc = 0
      return
    self.nr, self.nc = nr, nc
    self.dp = [matrix[ir][:] for ir in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if ir > 0:
          self.dp[ir][ic] += self.dp[ir - 1][ic]
        if ic > 0:
          self.dp[ir][ic] += self.dp[ir][ic - 1]
        if ir > 0 and ic > 0:
          self.dp[ir][ic] -= self.dp[ir - 1][ic - 1]

  """
  @param: row1: An integer
  @param: col1: An integer
  @param: row2: An integer
  @param: col2: An integer
  @return: An integer
  """

  def sumRegion(self, row1, col1, row2, col2):
    # write your code here
    v = self.dp[row2][col2]
    if row1 > 0:
      v -= self.dp[row1 - 1][col2]
    if col1 > 0:
      v -= self.dp[row2][col1 - 1]
    if row1 > 0 and col1 > 0:
      v += self.dp[row1 - 1][col1 - 1]
    return v


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

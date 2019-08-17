class NumMatrix(object):

  def __init__(self, matrix):
    """
    :type matrix: List[List[int]]
    """
    self.recsum = {}
    self.mods = {}
    self.matrix = matrix
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        tot = matrix[i][j]
        k = 0
        if i > 0:
          k += 1
          tot += self.recsum[(i - 1, j)]
        if j > 0:
          k += 1
          tot += self.recsum[(i, j - 1)]
        if k == 2:
          tot -= self.recsum[(i - 1, j - 1)]
        self.recsum[(i, j)] = tot

  def update(self, row, col, val):
    """
    :type row: int
    :type col: int
    :type val: int
    :rtype: void
    """
    self.mods[(row, col)] = val - self.matrix[row][col]

  def sumRegion(self, row1, col1, row2, col2):
    """
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    s = self.recsum[(row2, col2)]
    k = 0
    if row1 > 0:
      k += 1
      s -= self.recsum[(row1 - 1, col2)]
    if col1 > 0:
      k += 1
      s -= self.recsum[(row2, col1 - 1)]
    if k == 2:
      s += self.recsum[(row1 - 1, col1 - 1)]
    for (ir, ic) in self.mods:
      if (row1 <= ir <= row2 and col1 <= ic <= col2):
        s += self.mods[(ir, ic)]
    return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

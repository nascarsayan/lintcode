class Solution:
  """
  @param matrix: A lsit of lists of integers
  @return: nothing
  """

  def setZeroes(self, matrix):
    # write your code here
    nr = len(matrix)
    if nr == 0:
      return
    nc = len(matrix[0])
    if nc == 0:
      return
    ninf = float('-inf')
    for ir in range(nr):
      for ic in range(nc):
        if matrix[ir][ic] == 0:
          matrix[ir][ic] = ninf
    for ir in range(nr):
      for ic in range(nc):
        if matrix[ir][ic] == ninf:
          for icell in range(nr):
            if matrix[icell][ic] != ninf:
              matrix[icell][ic] = 0
          for jcell in range(nc):
            if matrix[ir][jcell] != ninf:
              matrix[ir][jcell] = 0
    for ir in range(nr):
      for ic in range(nc):
        if matrix[ir][ic] == ninf:
          matrix[ir][ic] = 0


# matrix = [[1, 0, 2], [4, 0, 6], [7, 8, 9]]
# Solution().setZeroes(matrix)
# print(matrix)

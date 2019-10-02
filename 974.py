class Solution:
  """
  @param matrix: a 0-1 matrix
  @return: return a matrix
  """

  def updateMatrix(self, matrix):
    # write your code here
    nr, nc, inf = len(matrix), len(matrix[0]), float('inf')
    for ir in range(nr):
      for ic in range(nc):
        if matrix[ir][ic] == 0:
          continue
        matrix[ir][ic] = inf
        if ir > 0:
          matrix[ir][ic] = min(matrix[ir][ic], matrix[ir - 1][ic] + 1)
        if ic > 0:
          matrix[ir][ic] = min(matrix[ir][ic], matrix[ir][ic - 1] + 1)
    for ir in range(nr)[::-1]:
      for ic in range(nc)[::-1]:
        if matrix[ir][ic] == 0:
          continue
        if ir < nr - 1:
          matrix[ir][ic] = min(matrix[ir][ic], matrix[ir + 1][ic] + 1)
        if ic < nc - 1:
          matrix[ir][ic] = min(matrix[ir][ic], matrix[ir][ic + 1] + 1)
    return matrix

class Solution:
  """
  @param matrix: a matrix
  @return: the minimum height
  """

  def minPathSumII(self, matrix):
    # Write your code here
    try:
      nr, nc = len(matrix), len(matrix[0])
    except IndexError:
      return 0
    for ir in range(nr)[::-1]:
      for ic in range(nc):
        if ir == nr - 1 and ic == 0:
          continue
        mn = float('inf')
        if ir < nr - 1:
          mn = min(mn, matrix[ir + 1][ic])
        if ic > 0:
          mn = min(mn, matrix[ir][ic - 1])
        matrix[ir][ic] += mn
    return matrix[0][-1]

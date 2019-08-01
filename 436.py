class Solution:
  """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

  def maxSquare(self, matrix):
    # write your code here
    nr = len(matrix)
    nc = len(matrix[0])
    if nr == 0 or nc == 0:
      return 0
    mar = max(matrix[0])
    mar = max([r[0] for r in matrix] + [mar])
    for i in range(1, nr):
      for j in range(1, nc):
        if matrix[i][j] == 0:
          continue
        matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1],
                           matrix[i][j - 1]) + 1
        mar = max(mar, matrix[i][j])
    return mar * mar


# print(Solution().maxSquare([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1],
#                             [1, 0, 0, 1, 0]]))
# print(Solution().maxSquare([[1, 1, 1, 1]]))

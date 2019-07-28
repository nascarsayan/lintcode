class Solution:

  def swap(self, matrix, i1, j1, i2, j2):
    matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

  """
    @param matrix: a lists of integers
    @return: nothing
    """

  def rotate(self, matrix):
    # write your code here
    size = len(matrix)
    if size == 0:
      return matrix
    for depth in range(size // 2):
      for pos in range(size - 2 * depth - 1):
        i1, j1 = depth, depth + pos
        self.swap(matrix, i1, j1, depth + pos, size - 1 - depth)
        self.swap(matrix, i1, j1, size - 1 - depth, size - 1 - depth - pos)
        self.swap(matrix, i1, j1, size - 1 - depth - pos, depth)
    return matrix


# print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

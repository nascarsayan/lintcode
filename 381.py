class Solution:
  """
  @param n: An integer
  @return: a square matrix
  """

  def generateMatrix(self, n):
    # write your code here
    matrix = [[None] * n for _ in range(n)]
    dep = 0
    v = 1
    while (dep < (n + 1) // 2):
      for j in range(dep, n - dep):
        matrix[dep][j] = v
        v += 1
      for i in range(dep + 1, n - dep):
        matrix[i][n - dep - 1] = v
        v += 1
      for j in range(n - dep - 2, dep - 1, -1):
        matrix[n - dep - 1][j] = v
        v += 1
      for i in range(n - dep - 2, dep, -1):
        matrix[i][dep] = v
        v += 1
      dep += 1
    return matrix


# print(Solution().generateMatrix(4))

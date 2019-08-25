class Solution:
  """
  @param matrix: the given matrix
  @return: the largest possible sum
  """

  def maxSubmatrix(self, matrix):
    # write your code here
    def kadane(arr):
      mx = float('-inf')
      tot = 0
      for el in arr:
        tot += el
        mx = max(mx, tot)
        if tot < 0:
          tot = 0
      return mx

    size = len(matrix)
    if size == 0 or len(matrix[0]) == 0:
      return 0
    bars = [matrix[ir][:] for ir in range(size)]
    for ir in range(1, size):
      for ic in range(size):
        bars[ir][ic] += bars[ir - 1][ic]
    bars.insert(0, [0] * size)
    mx = float('-inf')
    for st in range(size):
      for fl in range(st + 1, size + 1):
        arr = [bars[fl][ic] - bars[st][ic] for ic in range(size)]
        mx = max(mx, kadane(arr))
    return mx


print(Solution().maxSubmatrix([[1, 3, -1], [2, 3, -2], [-1, -2, -3]]))

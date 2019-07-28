class Solution:
  """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

  def minimumTotal(self, triangle):
    # write your code here
    size = len(triangle)
    if size == 0:
      return 0
    for ir in range(size - 2, -1, -1):
      for ic in range(ir + 1):
        triangle[ir][ic] += min(triangle[ir + 1][ic], triangle[ir + 1][ic + 1])
    return triangle[0][0]


# print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

class Solution:
  """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

  def maximalRectangle(self, matrix):
    # write your code here
    # mar = 0
    # nr = len(matrix)
    # if nr == 0:
    #   return 0
    # nc = len(matrix[0])
    # if nc == 0:
    #   return 0
    # reach = [[0, 0] * nc for _ in range(nr)]  # left, top
    # for ir in range(nr):
    #   for ic in range(nc):
    #     mv = matrix[ir][ic]
    #     reach[ir][ic] = [mv, mv]
    #     if ic > 0 and mv > 0:
    #       reach[ir][ic][0] = (reach[ir][ic - 1][0] + 1)
    #     if ir > 0 and mv > 0:
    #       reach[ir][ic][1] = (reach[ir - 1][ic][1] + 1)
    #     mar = max(reach[ir][ic] + [mar])
    # for ir in range(nr):
    #   for ic in range(nc):
    #     for ht in range()
    # return mar
    return


print(Solution().maximalRectangle([[1, 1, 0, 0, 1], [0, 1, 0, 0, 1],
                                   [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                   [0, 0, 0, 0, 1]]))
# print(Solution().maximalRectangle([[0, 0], [0, 0]]))

# !TLE
# def maximalRectangle(self, matrix):
#   # write your code here
#   mar = 0
#   nr = len(matrix)
#   if nr == 0:
#     return 0
#   nc = len(matrix[0])
#   if nc == 0:
#     return 0
#   reach = [[0, 0] * nc for _ in range(nr)]  # left, top
#   for ir in range(nr):
#     for ic in range(nc):
#       mv = matrix[ir][ic]
#       reach[ir][ic] = [mv, mv]
#       if ic > 0 and mv > 0:
#         reach[ir][ic][0] = (reach[ir][ic - 1][0] + 1)
#       if ir > 0 and mv > 0:
#         reach[ir][ic][1] = (reach[ir - 1][ic][1] + 1)
#   rects = [[[] for _ in range(nc)] for __ in range(nr)]
#   for ir in range(nr):
#     for ic in range(nc):
#       if matrix[ir][ic] == 0:
#         continue
#       if ic > 0:
#         lrects = rects[ir][ic - 1]
#         for lrect in lrects:
#           rects[ir][ic].append(
#               [lrect[0] + 1, min(lrect[1], reach[ir][ic][1])])
#       if ir > 0 and reach[ir][ic][1] > 1:
#         rects[ir][ic].append([1, reach[ir][ic][1]])
#       if reach[ir][ic] == [1, 1]:
#         rects[ir][ic].append([1, 1])
#       mar = max([dim[0] * dim[1] for dim in rects[ir][ic]] + [mar])
#       if ir > 0:
#         rects[ir - 1][ic] = []
#   return mar

class Solution:
  """
  @param matrix: the given matrix
  @return: The list of grid coordinates
  """

  def pacificAtlantic(self, matrix):
    # write your code here
    res = []
    try:
      nr, nc = len(matrix), len(matrix[0])
    except Exception:
      return res
    inf = float('inf')
    paci = [[matrix[ir][ic] for ic in range(nc)] for ir in range(nr)]
    atla = [[matrix[ir][ic] for ic in range(nc)] for ir in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if ir > 0 and ic > 0:
          paci[ir][ic] = inf
        if ir > 0:
          paci[ir][ic] = min(paci[ir][ic], paci[ir - 1][ic])
        if ic > 0:
          paci[ir][ic] = min(paci[ir][ic], paci[ir][ic - 1])
        if paci[ir][ic] > matrix[ir][ic]:
          paci[ir][ic] = inf
        else:
          paci[ir][ic] = max(paci[ir][ic], matrix[ir][ic])
    for ir in range(nr)[::-1]:
      for ic in range(nc)[::-1]:
        if ir < nr - 1 and ic < nc - 1:
          atla[ir][ic] = inf
        if ir < nr - 1:
          atla[ir][ic] = min(atla[ir][ic], atla[ir + 1][ic])
        if ic < nc - 1:
          atla[ir][ic] = min(atla[ir][ic], atla[ir][ic + 1])
        if atla[ir][ic] > matrix[ir][ic]:
          atla[ir][ic] = inf
        else:
          atla[ir][ic] = max(atla[ir][ic], matrix[ir][ic])
    for ir in range(nr):
      for ic in range(nc):
        if max(paci[ir][ic], atla[ir][ic]) <= matrix[ir][ic]:
          res.append([ir, ic])
    print('\n'.join(list(map(str, paci))), end='\n\n\n')
    print('\n'.join(list(map(str, atla))))
    return res


print(Solution().pacificAtlantic(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
     [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 12],
     [39, 72, 73, 74, 75, 76, 77, 78, 79, 50, 13],
     [38, 71, 96, 97, 98, 99, 100, 101, 80, 51, 14],
     [37, 70, 95, 112, 113, 114, 115, 102, 81, 52, 15],
     [36, 69, 94, 111, 120, 121, 116, 103, 82, 53, 16],
     [35, 68, 93, 110, 119, 118, 117, 104, 83, 54, 17],
     [34, 67, 92, 109, 108, 107, 106, 105, 84, 55, 18],
     [33, 66, 91, 90, 89, 88, 87, 86, 85, 56, 19],
     [32, 65, 64, 63, 62, 61, 60, 59, 58, 57, 20],
     [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]]))

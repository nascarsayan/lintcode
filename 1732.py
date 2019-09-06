class Solution:
  """
    @param board: board
    @return: snakesAndLadders
    """

  def snakesAndLadders(self, board):
    #
    size = len(board)
    if size == 0 or len(board[0]) == 0:
      return 0
    grsz = size * size
    vert = [0] * grsz
    for ir in range(size):
      for ic in range(size):
        v = (size - 1 - ir) * size + (ic,
                                      size - 1 - ic)[(size - 1 - ir) % 2 == 1]
        vert[v] = board[ir][ic] - 1
    visited = {0}
    que = [(0, 0)]
    while (len(que) > 0):
      u, dist = que.pop(0)
      if u == grsz - 1:
        return dist
      for du in range(1, 7):
        v = u + du
        if v >= grsz:
          break
        v = (v, vert[v])[vert[v] >= 0]
        if v in visited:
          continue
        que.append((v, dist + 1))
        visited.add(v)
    return -1


print(Solution().snakesAndLadders([[-1, 5, 14, -1], [-1, -1, -1, -1],
                                   [13, 11, 3, 10], [-1, -1, -1, -1]]))

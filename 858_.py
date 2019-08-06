class Solution:
  """
    @param board: a 2D integer array
    @return: the current board
    """

  def candyCrush(self, board):
    # Write your code here
    def crush(ir, ic, cnt, chang):
      if (ir < 0 or ir >= nr or ic < 0 or ic >= nc or board[ir][ic] != v or
          visited[ir][ic]):
        return cnt
      cnt += 1
      visited[ir][ic] = True
      cnt = max(cnt, crush(ir, ic - 1, cnt, chang))
      cnt = max(cnt, crush(ir - 1, ic, cnt, chang))
      cnt = max(cnt, crush(ir, ic + 1, cnt, chang))
      cnt = max(cnt, crush(ir + 1, ic, cnt, chang))
      if cnt > 2:
        board[ir][ic] = 0
        chang[0] = True
      return cnt

    nr = len(board)
    if nr == 0:
      return board
    nc = len(board[0])
    if nc == 0:
      return board
    visited = [[False] * nc for _ in range(nr)]
    while (True):
      chang = [False]
      for ir in range(nr):
        for ic in range(nc):
          v = board[ir][ic]
          if v != 0:
            crush(ir, ic, 0, chang)
      print(board)
      if not chang[0]:
        break
    for ic in range(nc):
      newc = list(filter(lambda x: x != 0, [board[ir][ic] for ir in range(nr)]))
      newcl = len(newc)
      for ir in range(nr - newcl):
        board[ir][ic] = 0
      for ir in range(nr - newcl, nr):
        board[ir][ic] = newc[nr - newcl - ir]
    return board


# !Wrong logic

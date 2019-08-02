class Solution:
  """
    @param board: the given board
    @return: nothing
    """

  def gameOfLife(self, board):
    # Write your code here
    nr = len(board)
    if nr == 0:
      return
    nc = len(board[0])
    if nc == 0:
      return
    nex = [[0] * nc for _ in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        live = sum([
            board[x][y]
            for x in range(ir - 1, ir + 2)
            for y in range(ic - 1, ic + 2)
            if (x >= 0 and x < nr and y >= 0 and y < nc and
                (x != ir or y != ic))
        ])
        if board[ir][ic] == 1:
          if live > 1 and live < 4:
            nex[ir][ic] = 1
        else:
          if live == 3:
            nex[ir][ic] = 1
    for ir in range(nr):
      for ic in range(nc):
        board[ir][ic] = nex[ir][ic]

class Solution:
  """
  @param board: a board
  @param click: the position
  @return: the new board
  """

  def updateBoard(self, board, click):
    # Write your code here
    def recurse(ir, ic):
      if board[ir][ic] not in ['E', 'M']:
        return
      if board[ir][ic] == 'M':
        board[ir][ic] = 'X'
        return
      cnt = sum(((0, 1)[board[ir + dr][ic + dc] in ['M', 'X']])
                for dr, dc in dif
                if (0 <= ir + dr < nr and 0 <= ic + dc < nc))
      if cnt == 0:
        board[ir][ic] = 'B'
        for dr, dc in dif:
          if (0 <= ir + dr < nr and 0 <= ic + dc < nc):
            recurse(ir + dr, ic + dc)
      else:
        board[ir][ic] = str(cnt)

    nr = len(board)
    if nr == 0:
      return board
    nc = len(board[0])
    if nc == 0:
      return board
    board = [list(row) for row in board]
    dif = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    ir, ic = click
    recurse(ir, ic)
    return [''.join(row) for row in board]


print(Solution().updateBoard(["EEEEE", "EEMEE", "EEEEE", "EEEEE"], [3, 0]))

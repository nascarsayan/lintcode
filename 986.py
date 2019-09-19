class Solution:
  """
  @param board: the given 2D board
  @return: the number of battle ships
  """

  def countBattleships(self, board):
    # Write your code here
    cnt = 0
    nr = len(board)
    if nr == 0:
      return 0
    nc = len(board[0])
    if nc == 0:
      return 0
    for ir in range(nr):
      for ic in range(nc):
        if board[ir][ic] == 'X' and not (
            (ir != 0 and board[ir - 1][ic] == 'X') or
            (ic != 0 and board[ir][ic - 1] == 'X')):
          cnt += 1
    return cnt


print(Solution().countBattleships(["X..X", "...X", "...X"]))

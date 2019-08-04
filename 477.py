class Solution:
  """
  @param: board: board a 2D board containing 'X' and 'O'
  @return: nothing
  """

  def surroundedRegions(self, board):
    # write your code here
    def escape(i, j):
      if (not (0 <= i < nr and 0 <= j < nc) or (i, j) in visited or
          board[i][j] != 'O'):
        return
      visited.add((i, j))
      board[i][j] = 'L'
      escape(i, j - 1)
      escape(i - 1, j)
      escape(i, j + 1)
      escape(i + 1, j)

    nr = len(board)
    if nr == 0:
      return
    nc = len(board[0])
    if nc == 0:
      return
    visited = set()
    for ir in range(nr):
      escape(ir, 0)
      escape(ir, nc - 1)
    for ic in range(1, nc - 1):
      escape(0, ic)
      escape(nr - 1, ic)
    for ir in range(nr):
      for ic in range(nc):
        if board[ir][ic] == 'L':
          board[ir][ic] = 'O'
        elif board[ir][ic] == 'O':
          board[ir][ic] = 'X'


# x = [list("XXXXX"), list("XXXXX"), list("XXOOX"), list("XXOXX"), list("XXOXX")]
# Solution().surroundedRegions(x)
# print(x)

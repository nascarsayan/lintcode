class Solution:
  """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """

  def validTicTacToe(self, board):
    # Write your code
    x, o = [], []

    def recurse(xo, typ):
      opp = (typ + 1) & 1
      l0 = len(xo[typ])
      l1 = len(xo[opp])
      if l0 + l1 == 0:
        return True
      if l0 == 0:
        return False
      for i, idx in enumerate(xo[typ]):
        bd[idx[0]][idx[1]] = typ
        vecs = [bd[idx[0]][:], [x[idx[1]] for x in bd]]
        if idx[0] == idx[1]:
          vecs.append([bd[i][i] for i in range(3)])
        if idx[0] + idx[1] == 2:
          vecs.append([bd[i][2 - i] for i in range(3)])
        if any(sum(vec) == 3 * typ for vec in vecs):
          bd[idx[0]][idx[1]] = inf
          return (l0 == 1 and l1 == 0)
        xo2 = [xo[0][:], xo[1][:]]
        xo2[typ].pop(i)
        v = recurse(xo2, opp)
        bd[idx[0]][idx[1]] = inf
        if v:
          return True
      return False

    for ir in range(3):
      for ic in range(3):
        if board[ir][ic] == 'X':
          x.append([ir, ic])
        elif board[ir][ic] == 'O':
          o.append([ir, ic])
    inf = float('inf')
    bd = [[inf] * 3 for _ in range(3)]
    return recurse([x, o], 0)


print(Solution().validTicTacToe(["OOX", " XO", "X  "]))

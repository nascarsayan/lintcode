class Solution:

  def recurse(self, n, row, filled, seq, permuts):
    if row == n:
      permuts.append(seq)
      return
    for col in range(n):
      if (filled[col] == 0):
        diag = False
        for pi, pj in enumerate(seq):
          if (row - pi == abs(col - pj)):
            diag = True
        if diag:
          continue
        filled[col] = 1
        self.recurse(n, row + 1, filled, seq + [col], permuts)
        filled[col] = 0

  """
    @param: n: The number of queens
    @return: All distinct solutions
    """

  def solveNQueens(self, n):
    # write your code here
    permuts = []
    self.recurse(n, 0, [0] * n, [], permuts)
    lp = len(permuts)
    boards = [['.' * n] * n for _ in range(lp)]
    for ip, permut in enumerate(permuts):
      for ir, ic in enumerate(permut):
        boards[ip][ir] = '%sQ%s' % ('.' * ic, '.' * (n - ic - 1))
    return boards


# print(Solution().solveNQueens(4))
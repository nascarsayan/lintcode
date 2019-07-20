class Solution:

  def recurse(self, n, row, filled, seq, permuts):
    if row == n:
      permuts[0] += 1
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
  @param n: The number of queens.
  @return: The total number of distinct solutions.
  """

  def totalNQueens(self, n):
    # write your code here
    permuts = [0]
    self.recurse(n, 0, [0] * n, [], permuts)
    return permuts[0]


# print(Solution().totalNQueens(4))
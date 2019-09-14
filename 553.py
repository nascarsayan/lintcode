class Solution:
  """
  @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
  @return: an integer, the maximum enemies you can kill using one bomb
  """

  def maxKilledEnemies(self, grid):
    # write your code here
    mp = {'0': 0, 'W': 0, 'E': 1}

    def newgr(nr, nc):
      return [[mp[grid[ir][ic]] for ic in range(nc)] for ir in range(nr)]

    nr = len(grid)
    if nr == 0:
      return 0
    nc = len(grid[0])
    if nc == 0:
      return 0
    L = newgr(nr, nc)
    U = newgr(nr, nc)
    R = newgr(nr, nc)
    D = newgr(nr, nc)
    for ir in range(nr):
      for ic in range(nc):
        if grid[ir][ic] == 'W':
          continue
        if ic > 0:
          L[ir][ic] += L[ir][ic - 1]
        if ir > 0:
          U[ir][ic] += U[ir - 1][ic]
    for ir in range(nr)[::-1]:
      for ic in range(nc)[::-1]:
        if grid[ir][ic] == 'W':
          continue
        if ic < nc - 1:
          R[ir][ic] += R[ir][ic + 1]
        if ir < nr - 1:
          D[ir][ic] += D[ir + 1][ic]
    mx = 0
    for ir in range(nr):
      for ic in range(nc):
        if grid[ir][ic] == '0':
          mx = max(mx, sum(dp[ir][ic] for dp in [L, U, R, D]))
    return mx


print(Solution().maxKilledEnemies(["0E00", "E0WE", "0E00"]))

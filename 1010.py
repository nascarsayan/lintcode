class Solution:
  """
  @param grid: a 2D array
  @return: the maximum total sum that the height of the buildings can be increased
  """

  def maxIncreaseKeepingSkyline(self, grid):
    # Write your code here
    nr = len(grid)
    if nr == 0:
      return 0
    nc = len(grid[0])
    if nc == 0:
      return 0
    mxi = 0
    vert = [None] * nr
    hori = [None] * nc
    for ir in range(nr):
      vert[ir] = max(grid[ir])
    for ic in range(nc):
      hori[ic] = max([x[ic] for x in grid])
    for ir in range(nr):
      for ic in range(nc):
        mxi += min(vert[ir], hori[ic]) - grid[ir][ic]
    return mxi

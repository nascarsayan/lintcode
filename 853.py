from collections import defaultdict
import bisect

# !TLE


class Solution:
  """
    @param grid: the grid
    @return: the number of corner rectangles
    """

  def countCornerRectangles(self, grid):
    # Write your code here
    nr = len(grid)
    if nr == 0:
      return 0
    nc = len(grid[0])
    if nc == 0:
      return 0
    tot = 0
    r1, c1 = defaultdict(list), defaultdict(list)
    for ir in range(nr):
      for ic in range(nc):
        if grid[ir][ic] == 1:
          r1[ir].append(ic)
          c1[ic].append(ir)

    rows = sorted(r1.keys())
    for pr, ir in enumerate(rows):
      for pc, ic in enumerate(r1[ir]):
        if pr == 0 or pc == 0:
          continue
        currc = set(r1[ir][:pc])
        for qr in range(pr):
          qc = bisect.bisect_left(r1[rows[qr]], ic)
          if qc >= len(r1[rows[qr]]) or r1[rows[qr]][qc] != ic:
            continue
          tot += len(set(r1[rows[qr]]).intersection(currc))

    return tot


print(Solution().countCornerRectangles())

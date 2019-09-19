from collections import deque


class Solution:
  """
  @param grid: a 2d boolean array
  @param k: an integer
  @return: the number of Islands
  """

  def numsofIsland(self, grid, k):
    # Write your code here
    try:
      nr, nc = len(grid), len(grid[0])
    except IndexError:
      return 0
    isls = 0
    visited = [[False] * nc for _ in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if grid[ir][ic] == 0 or visited[ir][ic]:
          continue
        que, sz = deque([(ir, ic)]), 0
        visited[ir][ic] = True
        while (que):
          jr, jc = que.popleft()
          sz += 1
          for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            kr, kc = jr + dr, jc + dc
            if not (0 <= kr < nr and
                    0 <= kc < nc) or visited[kr][kc] or grid[kr][kc] == 0:
              continue
            que.append((kr, kc))
            visited[kr][kc] = True
        if sz >= k:
          isls += 1
    return isls


print(Solution().numsofIsland(
    [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1]], 2))

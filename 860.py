from collections import deque


class Solution:
  """
  @param grid: a list of lists of integers
  @return: return an integer, denote the number of distinct islands
  """

  def numberofDistinctIslands(self, grid):
    # write your code here
    try:
      nr, nc = len(grid), len(grid[0])
    except IndexError:
      return 0
    isls = set()
    visited = [[False] * nc for _ in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if grid[ir][ic] == 0 or visited[ir][ic]:
          continue
        que = deque([(ir, ic)])
        cells = []
        while que:
          jr, jc = que.popleft()
          cells.append((jr - ir, jc - ic))
          visited[jr][jc] = True
          for dr, dc in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            kr, kc = jr + dr, jc + dc
            if not (0 <= kr < nr and
                    0 <= kc < nc) or grid[kr][kc] == 0 or visited[kr][kc]:
              continue
            visited[kr][kc] = True
            que.append((kr, kc))
        isls.add(tuple(cells))
    return len(isls)


print(Solution().numberofDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                                          [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))

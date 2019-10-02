from collections import deque


class Solution:
  """
  @param maze: the maze
  @param start: the start
  @param destination: the destination
  @return: the shortest distance for the ball to stop at the destination
  """

  def shortestDistance(self, maze, start, destination):
    # write your code here
    try:
      nr, nc = len(maze), len(maze[0])
    except IndexError:
      return 0
    # inf = float('inf')
    start, destination = tuple(start), tuple(destination)
    dist = [[[0] * 4 for ic in range(nc)] for ir in range(nr)]  # LURD
    for ir in range(nr):
      for ic in range(nc):
        if maze[ir][ic] == 1:
          dist[ir][ic][0] = dist[ir][ic][1] = dist[ir][ic][2] = dist[ir][ic][
              3] = -1
          continue
        if ic > 0:
          dist[ir][ic][0] = dist[ir][ic - 1][0] + 1
        if ir > 0:
          dist[ir][ic][1] = dist[ir - 1][ic][1] + 1
    for ir in range(nr)[::-1]:
      for ic in range(nc)[::-1]:
        if maze[ir][ic] == 1:
          continue
        if ic < nc - 1:
          dist[ir][ic][2] = dist[ir][ic + 1][2] + 1
        if ir < nr - 1:
          dist[ir][ic][3] = dist[ir + 1][ic][3] + 1
    que = deque([(start, 0)])
    visited = [[False] * nc for ir in range(nr)]
    visited[start[0]][start[1]] = True
    while (que):
      (ir, ic), d = que.popleft()
      if (ir, ic) == destination:
        return d
      for dr, dc in [[0, -dist[ir][ic][0]], [-dist[ir][ic][1], 0],
                     [0, dist[ir][ic][2]], [dist[ir][ic][3], 0]]:
        jr, jc = ir + dr, ic + dc
        if not (0 <= ir < nr and 0 <= ic < nc) or visited[jr][jc]:
          continue
        visited[jr][jc] = True
        que.append(((jr, jc), d + abs(dr + dc)))
    return -1


print(Solution().shortestDistance(
    [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
     [0, 0, 0, 0, 0]], [0, 4], [4, 4]))

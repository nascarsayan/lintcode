from collections import deque


class Solution:
  """
  @param maze: the maze
  @param start: the start
  @param destination: the destination
  @return: whether the ball could stop at the destination
  """

  def hasPath(self, maze, start, destination):
    # write your code here
    nr = len(maze)
    nc = len(maze[0])

    def makeMat(nr, nc):
      return [[-1] * nc for _ in range(nr)]

    L, U, R, D = [makeMat(nr, nc) for _ in range(4)]
    ux, uy = start
    vx, vy = destination
    if start == destination:
      return True
    if maze[ux][uy] == 1 or maze[vx][vy] == 1:
      return False
    for ir in range(nr):
      for ic in range(nc):
        if maze[ir][ic] == 1:
          continue
        if ic == 0:
          L[ir][ic] = 0
        else:
          L[ir][ic] = L[ir][ic - 1] + 1
        if ir == 0:
          U[ir][ic] = 0
        else:
          U[ir][ic] = U[ir - 1][ic] + 1

    for ir in range(nr)[::-1]:
      for ic in range(nc)[::-1]:
        if maze[ir][ic] == 1:
          continue
        if ic == nc - 1:
          R[ir][ic] = 0
        else:
          R[ir][ic] = R[ir][ic + 1] + 1
        if ir == nr - 1:
          D[ir][ic] = 0
        else:
          D[ir][ic] = D[ir + 1][ic] + 1

    que = deque([(ux, uy)])
    visited = [[False] * nc for _ in range(nr)]
    while (que):
      # print(que)
      cx, cy = que.popleft()
      if (cx, cy) == (vx, vy):
        return True
      dl, du, dr, dd = L[cx][cy], U[cx][cy], R[cx][cy], D[cx][cy]
      for dst, (mx, my) in [(dl, (0, -1)), (du, (-1, 0)), (dr, (0, 1)),
                            (dd, (1, 0))]:
        if dst > 0:
          nx, ny = cx + mx * dst, cy + my * dst
          if not visited[nx][ny]:
            que.append((nx, ny))
            visited[nx][ny] = True
    return False


print(Solution().hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                          [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))

from collections import deque


class Solution:
  """
  @param matrix : the martix
  @return: the distance of grid to the police
  """

  def policeDistance(self, matrix):
    # Write your code here
    nr = len(matrix)
    if nr == 0:
      return matrix
    nc = len(matrix[0])
    if nc == 0:
      return matrix
    inf = float('inf')
    dist = [[inf] * nc for _ in range(nr)]
    que = deque()
    visited = [[False] * nc for _ in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if matrix[ir][ic] == 1:
          visited[ir][ic] = True
          dist[ir][ic] = 0
          que.append((ir, ic))

    while (que):
      ir, ic = que.popleft()
      for dr, dc in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
        jr, jc = ir + dr, ic + dc
        if not (0 <= jr < nr and
                0 <= jc < nc) or visited[jr][jc] or matrix[jr][jc] != 0:
          continue
        visited[jr][jc] = True
        dist[jr][jc] = dist[ir][ic] + 1
        que.append((jr, jc))
    for ir in range(nr):
      for ic in range(nc):
        if dist[ir][ic] == inf:
          dist[ir][ic] = -1
    return dist

from collections import deque


class Solution:
  """
  @param maps:
  @return: nothing
  """

  def theMazeIV(self, maps):
    #
    try:
      nr, nc = len(maps), len(maps[0])
    except IndexError:
      return -1
    starr, flarr = [], []
    visited = [[False] * nc for ir in range(nr)]
    for ir in range(nr):
      for ic in range(nc):
        if maps[ir][ic] == 'S':
          starr.append((ir, ic))
          visited[ir][ic] = True
        elif maps[ir][ic] == 'T':
          flarr.append((ir, ic))
    if not flarr:
      return -1
    que = deque([(st, 0) for st in starr])
    while (que):
      (ir, ic), d = que.popleft()
      if maps[ir][ic] == 'T':
        return d
      for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        jr, jc = ir + dr, ic + dc
        if not (0 <= jr < nr and
                0 <= jc < nc) or maps[jr][jc] == '#' or visited[jr][jc]:
          continue
        visited[jr][jc] = True
        que.append(((jr, jc), d + 1))
    return -1

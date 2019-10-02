from collections import deque


class Solution:

  def ShortestBridge(self, A):
    try:
      nr, nc = len(A), len(A[0])
    except IndexError:
      return 0
    i1r, i1c = None, None
    for ir in range(nr):
      for ic in range(nc):
        if A[ir][ic] == 1:
          i1r, i1c = ir, ic
          break
      if i1r is not None:
        break
    que = deque([(i1r, i1c)])
    frontier = deque()
    visited = [[False] * nc for ir in range(nr)]
    visited[i1r][i1c] = True
    while (que):
      ir, ic = que.popleft()
      neis = [(jr, jc) for jr, jc in [(ir + dr, ic + dc) for dr, dc in [(
          0, -1), (-1, 0), (0, 1), (1, 0)]] if (0 <= jr < nr and 0 <= jc < nc)]
      for jr, jc in neis:
        if not visited[jr][jc] and A[jr][jc] == 1:
          visited[jr][jc] = True
          que.append((jr, jc))
        if A[jr][jc] == 0:
          frontier.append(((jr, jc), 0))
          visited[jr][jc] = True
    while(frontier):
      (ir, ic), d = frontier.popleft()
      if A[ir][ic] == 1:
        return d
      neis = [(jr, jc) for jr, jc in [(ir + dr, ic + dc) for dr, dc in [(
          0, -1), (-1, 0), (0, 1), (1, 0)]] if (0 <= jr < nr and 0 <= jc < nc)]
      for jr, jc in neis:
        if not visited[jr][jc]:
          visited[jr][jc] = True
          frontier.append(((jr, jc), d + 1))
    return None


print(Solution().ShortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))

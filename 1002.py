from collections import defaultdict


class Solution:
  """
  @param routes:  a list of bus routes
  @param S: start
  @param T: destination
  @return: the least number of buses we must take to reach destination
  """

  def numBusesToDestination(self, routes, S, T):
    # Write your code here
    def bfs(ib):
      que = [(ib, 0)]
      while (len(que) > 0):
        b, d = que.pop(0)
        if T in stops[b]:
          return d + 1
        visited[b] = True
        for ne in graph[b]:
          if not visited[ne]:
            que.append((ne, d + 1))
      return inf

    if S == T:
      return 0
    inf = float('inf')
    nbus = len(routes)
    stops = [None] * nbus
    graph = defaultdict(list)
    for ib in range(nbus):
      stops[ib] = set(routes[ib])
    for ib1 in range(nbus):
      for ib2 in range(ib1 + 1, nbus):
        if len(stops[ib1].intersection(stops[ib2])) > 0:
          graph[ib1].append(ib2)
          graph[ib2].append(ib1)
    visited = [False] * nbus
    mindist = inf
    for ib in range(nbus):
      if S not in stops[ib] or visited[ib]:
        continue
      dist = bfs(ib)
      mindist = min(mindist, dist)
    return (mindist, -1)[mindist == inf]


print(Solution().numBusesToDestination([[2], [8, 2]], 8, 2))

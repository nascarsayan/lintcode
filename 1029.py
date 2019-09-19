import heapq


class Solution:
  """
  @param n: a integer
  @param flights: a 2D array
  @param src: a integer
  @param dst: a integer
  @param K: a integer
  @return: return a integer
  """

  def findCheapestPrice(self, n, flights, src, dst, K):
    # write your code here
    inf = float('inf')
    graph = [[inf] * n for _ in range(n)]
    for u, v, w in flights:
      graph[u][v] = w
    hp = []
    visited = [False] * n
    dist = [inf] * n
    heapq.heappush(hp, (0, 0, src))
    dist[src] = 0
    while (hp):
      d, stops, u = heapq.heappop(hp)
      visited[u] = True
      if u == dst:
        return d
      if stops > K:
        continue
      for v in range(n):
        if graph[u][v] == inf or visited[v]:
          continue
        ud = d + graph[u][v]
        if ud < dist[v]:
          dist[v] = ud
          heapq.heappush(hp, (ud, stops + 1, v))
    return -1


print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                   0, 2, 0))

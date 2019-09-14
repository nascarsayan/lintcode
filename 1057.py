class Solution:
  """
  @param times: a 2D array
  @param N: an integer
  @param K: an integer
  @return: how long will it take for all nodes to receive the signal
  """

  def networkDelayTime(self, times, N, K):
    # Write your code here
    inf = float('inf')
    ninf = float('-inf')
    graph = [[inf] * (N + 1) for _ in range(N + 1)]
    for u, v, w in times:
      graph[u][v] = min(graph[u][v], w)
    tottm = [inf] * (N + 1)
    tottm[K] = 0
    mst = set()
    while (True):
      u = 0
      for tu in range(1, N + 1):
        if tu not in mst and tottm[tu] < tottm[u]:
          u = tu
      if u == 0:
        break
      mst.add(u)
      for v in range(1, N + 1):
        tottm[v] = min(tottm[v], tottm[u] + graph[u][v])
    # print(graph)
    mx = ninf
    # print(tottm)
    for i in range(1, N + 1):
      if tottm[i] == inf:
        return -1
      mx = max(mx, tottm[i])
    return mx


# print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]],
#                                   3, 2))

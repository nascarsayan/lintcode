class Solution:
  """
  @param richer: the richer array
  @param quiet: the quiet array
  @return: the answer
  """

  def loudAndRich(self, richer, quiet):
    # Write your code here.
    def dfs(u):
      visited[u] = True
      mn = u
      for v in graph[u]:
        mnv = res[v]
        if not visited[v]:
          mnv = dfs(v)
        if quiet[mnv] < quiet[mn]:
          mn = mnv
      res[u] = mn
      return mn

    V = len(quiet)
    graph = [[] for _ in range(V)]
    for v, u in richer:
      graph[u].append(v)
    for u in range(V):
      graph[u] = list(sorted(set(graph[u])))
    visited = [False] * V
    res = [float('inf')] * V
    for u in range(V):
      if not visited[u]:
        dfs(u)
    return res


print(Solution().loudAndRich([[2, 3], [1, 4], [0, 4], [0, 3]], [0, 1, 3, 4, 2]))

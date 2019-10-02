class Solution:
  """
  @param n: The number of points
  @param G: The description of graph
  @param S: The point S
  @param T: The point T
  @return: output all the paths from S to T
  """

  def getPath(self, n, G, S, T):
    # Write your code here
    def dfs(path):
      if path[-1] == T:
        res.append(path)
        return
      for v in graph[path[-1]]:
        if v not in path:
          dfs(path + [v])

    graph = [set() for _ in range(n)]
    for u, v in G:
      graph[u].add(v)
      graph[v].add(u)
    for u in range(n):
      graph[u] = list(sorted(graph[u]))
    res = []
    dfs([S])
    return res


print(Solution().getPath(
    n=4, G=[[0, 1], [0, 2], [1, 2], [1, 3], [3, 2]], S=0, T=2))

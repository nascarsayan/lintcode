class Solution:
  """
  @param graph: a 2D array
  @return: all possible paths from node 0 to node N-1
  """

  def allPathsSourceTarget(self, graph):
    # Write your code here
    size = len(graph)
    paths = []
    if size == 0:
      return paths

    def dfs(u, path):
      if u == size - 1:
        paths.append(path + [u])
        return
      for v in graph[u]:
        if v not in path:
          dfs(v, path + [u])

    dfs(0, [])
    return paths


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))

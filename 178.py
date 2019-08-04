from collections import defaultdict


class Solution:
  """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

  def validTree(self, n, edges):
    # write your code here
    def dfs(curr, parent):
      if curr in visited:
        return False
      visited.add(curr)
      for nei in graph[curr]:
        if nei != parent:  # !don't use is not with anything other than None
          if not dfs(nei, curr):
            return False
      return True

    graph = defaultdict(list)
    for edge in edges:
      graph[edge[0]].append(edge[1])
      graph[edge[1]].append(edge[0])
    visited = set()
    if not dfs(0, None):
      return False
    if len(visited) != n:
      return False
    return True

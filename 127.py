"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
  """
  @param: graph: A list of Directed graph node
  @return: Any topological order for the given graph.
  """

  def topSort(self, graph):
    # write your code here
    res = []
    visited = set()

    def dfs(u):
      for nei in u.neighbors:
        if nei not in visited:
          visited.add(nei)
          dfs(nei)
      res.append(u)

    for u in graph:
      if u not in visited:
        visited.add(u)
        dfs(u)
    return list(reversed(res))

from collections import defaultdict
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
  @param: s: the starting Directed graph node
  @param: t: the terminal Directed graph node
  @return: a boolean value
  """

  def hasRoute(self, graph, s, t):
    # write your code here
    def dfs(u):
      visited[u] = True
      if u == t:
        return True
      for v in u.neighbors:
        if not visited[v]:
          if dfs(v):
            return True
      return False

    visited = defaultdict(bool)
    return dfs(s)

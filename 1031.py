class Solution:
  """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """

  def isBipartite(self, graph):
    # Write your code here
    def assgn(v, p):
      if grp[v] is not None:
        if grp[v] != p:
          return False
        return True
      grp[v] = p
      for ne in graph[v]:
        if not assgn(ne, (p + 1) % 2):
          return False
      return True

    nv = len(graph)
    if nv < 3:
      return True
    grp = [None] * nv
    for v in range(nv):
      if not assgn(v, (grp[v], 0)[grp[v] is None]):
        return False
    return True

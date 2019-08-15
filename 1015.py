from collections import defaultdict


class Solution:
  """
    @param graph: a 2D integers array
    @return: return a list of integers
    """

  def eventualSafeNodes(self, graph):
    # write your code here
    def isSafe(i, path):
      if i in unsafe:
        return False
      if i in safe:
        return True
      for ne in g[i]:
        if ne in path:
          unsafe.update(path)
          return False

        if not isSafe(ne, path.union([i])):
          return False
      safe.add(i)
      return True

    g = defaultdict(set)
    unsafe = set()
    for i in range(len(graph)):
      g[i] = set(graph[i])
    safe = set()
    for i in g:
      isSafe(i, set())
    return list(sorted(list(safe)))

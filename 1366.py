from collections import defaultdict


class Solution:
  """
  @param start: The start points set
  @param end: The end points set
  @return: Return if the graph is cyclic
  """

  def isCyclicGraph(self, start, end):
    # Write your code here
    graph = defaultdict(set)
    indeg = defaultdict(int)
    nv = 0
    for u, v in zip(start, end):
      if v not in graph[u]:
        graph[u].add(v)
        indeg[v] += 1
        nv = max([u, v, nv])
    que = []
    for v in range(1, nv + 1):
      if indeg[v] == 0:
        que.append(v)
    cnt = 0
    while (que):
      node = que.pop(-1)
      for nei in graph[node]:
        indeg[nei] -= 1
        if indeg[nei] == 0:
          que.append(nei)
      cnt += 1
    return cnt != nv


print(Solution().isCyclicGraph([1], [2]))

from collections import defaultdict


class Solution:
  """
  @param tickets:
  @return: nothing
  """

  def findItinerary(self, tickets):
    # Write your code here
    def dfs(path):
      u = path[-1]
      if len(path) == ne + 1:
        return path
      for v in graph[u]:
        if avail[u][v] > 0:
          avail[u][v] -= 1
          dpath = dfs(path + [v])
          avail[u][v] += 1
          if dpath is not None:
            return dpath
      return None

    ports = set()
    for u, v in tickets:
      ports.add(u)
      ports.add(v)
    ports = sorted(list(ports))
    p2idx = dict([(name, i) for i, name in enumerate(ports)])
    graph = defaultdict(list)
    nv = len(ports)
    ne = len(tickets)
    avail = [[0] * nv for _ in range(nv)]
    for u, v in tickets:
      graph[p2idx[u]].append(p2idx[v])
      avail[p2idx[u]][p2idx[v]] += 1
    for u in range(nv):
      graph[u] = list(sorted(set(graph[u])))
    return list(map(lambda idx: ports[idx], dfs([p2idx['JFK']])))


print(Solution().findItinerary([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"],
                                ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
                                ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"],
                                ["JFK", "TIA"]]))

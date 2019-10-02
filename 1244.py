from collections import deque


class Solution:
  """
  @param start:
  @param end:
  @param bank:
  @return: the minimum number of mutations needed to mutate from "start" to "end"
  """

  def minMutation(self, start, end, bank):
    # Write your code here
    bank = list(set([start] + bank))
    V = len(bank)
    if start == end:
      return 0
    if start != end and end not in bank:
      return -1
    st, fl = bank.index(start), bank.index(end)
    graph = [set() for u in range(V)]
    for u in range(V - 1):
      for v in range(u + 1, V):
        if sum(
            list(
                map(lambda x: 1
                    if x[0] != x[1] else 0, zip(bank[u], bank[v])))) == 1:
          graph[u].add(v)
          graph[v].add(u)
    visited = [False] * V
    que = deque([(st, 0)])
    visited[st] = True
    while (que):
      u, d = que.popleft()
      if u == fl:
        return d
      for v in graph[u]:
        if visited[v]:
          continue
        visited[v] = True
        que.append((v, d + 1))
    return -1

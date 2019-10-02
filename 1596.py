from collections import deque


class Solution:
  """
  @param N:  sum of the set
  @param dislikes: dislikes peoples
  @return:  if it is possible to split everyone into two groups in this way
  """

  def possibleBipartition(self, N, dislikes):
    # Write your code here.

    graph = [set() for _ in range(N + 1)]
    for u, v in dislikes:
      graph[u].add(v)
      graph[v].add(u)
    for u in range(1, N + 1):
      graph[u] = list(sorted(graph[u]))
    assign = [0] * (N + 1)
    for u in range(1, N + 1):
      if assign[u] != 0:
        continue
      assign[u] = 1
      que = deque([u])
      while (que):
        cu = que.popleft()
        for cv in graph[cu]:
          if assign[cv] == assign[cu]:
            return False
          if assign[cv] == -assign[cu]:
            continue
          assign[cv] = -assign[cu]
          que.append(cv)
    return True


# !DFS
# def possibleBipartition(self, N, dislikes):
#   # Write your code here.
#   def dfs(u, col):
#     if instac[u]:
#       return True
#     if assign[u] == -col:
#       return False
#     if assign[u] == col:
#       return True
#     instac[u] = True
#     assign[u] = col
#     for v in graph[u]:
#       if not dfs(v, -col):
#         return False
#     instac[u] = False
#     return True

#   graph = [set() for _ in range(N + 1)]
#   for u, v in dislikes:
#     graph[u].add(v)
#     graph[v].add(u)
#   for u in range(1, N + 1):
#     graph[u] = list(sorted(graph[u]))
#   assign = [0] * (N + 1)
#   for u in range(1, N + 1):
#     if assign[u] != 0:
#       continue
#     col = 1
#     instac = [False] * (N + 1)
#     if not dfs(u, col):
#       return False
#   return True

print(Solution().possibleBipartition(5,
                                     [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))

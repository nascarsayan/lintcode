from collections import defaultdict

from collections import deque


class Solution:
  """
  @param: numCourses: a total of n courses
  @param: prerequisites: a list of prerequisite pairs
  @return: true if can finish all courses or false
  """

  def canFinish(self, numCourses, prerequisites):

    nv = numCourses
    graph = defaultdict(set)
    indeg = [0] * nv
    que = deque()
    for u, v in prerequisites:
      if v not in graph[u]:
        graph[u].add(v)
        indeg[v] += 1
    for u in range(nv):
      if indeg[u] == 0:
        que.append(u)
    cnt = 0
    while (que):
      u = que.popleft()
      cnt += 1
      for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
          que.append(v)
    return cnt == nv


print(Solution().canFinish(
    10, [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]]))

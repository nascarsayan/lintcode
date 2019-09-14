from collections import deque


class Solution:
  """
  @param rooms: a list of keys rooms[i]
  @return: can you enter every room
  """

  def canVisitAllRooms(self, rooms):
    # Write your code here
    V = len(rooms)
    if V == 1:
      return True
    visited = [False] * V
    visited[0] = True
    que = deque([0])
    cnt = 0
    while (que):
      u = que.popleft()
      for v in rooms[u]:
        if not visited[v]:
          visited[v] = True
          cnt += v
          que.append(v)
      if cnt == (V * (V - 1)) // 2:
        return True
    return False

from collections import defaultdict


class Solution:
  """
  @param rooms: m x n 2D grid
  @return: nothing
  """

  def wallsAndGates(self, rooms):
    # write your code here
    nr = len(rooms)
    if nr == 0:
      return
    nc = len(rooms[0])
    if nc == 0:
      return
    que = []
    visited = defaultdict(bool)
    for ir in range(nr):
      for ic in range(nc):
        if rooms[ir][ic] == 0:
          que.append(((ir, ic), 0))
          visited[(ir, ic)] = True
    while (len(que) > 0):
      (ir, ic), d = que.pop(0)
      for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        jr, jc = ir + dr, ic + dc
        if not (0 <= jr < nr and
                0 <= jc < nc) or visited[(jr, jc)] or rooms[jr][jc] == -1:
          continue
        visited[(jr, jc)] = True
        rooms[jr][jc] = d + 1
        que.append(((jr, jc), d + 1))


arr = [[2147483647, -1, 0,
        2147483647], [2147483647, 2147483647, 2147483647, -1],
       [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
Solution().wallsAndGates(arr)
print(arr)

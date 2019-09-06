class Solution:
  """
  @param Maze:
  @return: nothing
  """

  def Portal(self, Maze):
    #
    nr, nc = len(Maze), len(Maze[0])
    que, visited = [], set()
    for ir in range(nr):
      for ic in range(nc):
        if Maze[ir][ic] == 'S':
          que.append(((ir, ic), 0))
          visited.add((ir, ic))
          break
    while (que):
      (ir, ic), d = que.pop(0)
      if Maze[ir][ic] == 'E':
        return d
      for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        jr, jc = ir + dr, ic + dc
        if not ((0 <= jr < nr) and
                (0 <= jc < nc)) or (jr, jc) in visited or Maze[jr][jc] == '#':
          continue
        visited.add((jr, jc))
        que.append(((jr, jc), d + 1))
    return -1


print(Solution().Portal(["S*E", "***", "#**", "##E"]))

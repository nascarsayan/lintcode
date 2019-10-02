class Solution:
  """
  @param height: the height
  @param width: the width
  @param tree: the position of tree
  @param squirrel: the position of squirrel
  @param nuts: the position of nuts
  @return: the minimal distance
  """

  def minDistance(self, height, width, tree, squirrel, nuts):
    # Write your code here
    dists = [abs(x - tree[0]) + abs(y - tree[1]) for x, y in nuts]
    ndist = sum(dists)
    return min([
        2 * ndist - 2 * dists[i] + abs(x - squirrel[0]) + abs(y - squirrel[1]) +
        dists[i] for i, (x, y) in enumerate(nuts)
    ])


# print(Solution().minDistance(5, 5, [3,2], [0,1], [[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],
# [0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]]))

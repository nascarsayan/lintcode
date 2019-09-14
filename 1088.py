class Subs:

  def __init__(self, parent, rank):
    self.parent = parent
    self.rank = rank

  def __repr__(self):
    return '(p:{}, r:{})'.format(self.parent, self.rank)


class Solution:
  """
  @param edges: List[List[int]]
  @return: List[int]
  """

  def findRedundantConnection(self, edges):
    # write your code here
    def find(node):
      if (subs[node].parent != node):
        subs[node].parent = find(subs[node].parent)
      return subs[node].parent

    def union(u, v):
      if subs[u].rank > subs[v].rank:
        subs[v].parent = u
      elif subs[u].rank < subs[v].rank:
        subs[u].parent = v
      else:
        subs[v].parent = u
        subs[u].rank += 1

    size = len(edges)
    subs = [None]
    for i in range(1, size + 1):
      subs.append(Subs(i, 0))
    for u, v in edges:
      uroot = find(u)
      vroot = find(v)
      if uroot == vroot:
        return [u, v]
      union(uroot, vroot)


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))

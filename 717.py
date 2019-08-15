from collections import defaultdict


class Solution:
  """
  @param A: as indicated in the description
  @param E: as indicated in the description
  @return: Return the number of edges on the longest path with same value.
  """

  def LongestPathWithSameValue(self, A, E):
    # write your code here
    def dfs(v, mx):
      if visited[v - 1]:
        return 0
      lns = [0]
      visited[v - 1] = True
      for ne in graph[v]:
        if A[ne - 1] == A[v - 1] and not visited[ne - 1]:
          lns.append(dfs(ne, mx) + 1)
      lns.sort()
      mx[0] = max(mx[0], lns[-1])
      if len(lns) > 1:
        mx[0] = max(mx[0], lns[-1] + lns[-2])
      return lns[-1]

    size = len(A)
    graph = defaultdict(set)
    for i in range(size - 1):
      graph[E[2 * i]].add(E[2 * i + 1])
      graph[E[2 * i + 1]].add(E[2 * i])
    visited = [False] * size
    mx = [0]
    for v in range(1, size + 1):
      if not visited[v - 1]:
        dfs(v, mx)
    return mx[0]


print(Solution().LongestPathWithSameValue([1, 1, 1, 2, 2],
                                          [1, 2, 1, 3, 2, 4, 2, 5]))

# !in case tree is given
# class TNode:

#   def __init__(self, num, label):
#     self.num = num
#     self.label = label
#     self.left = None
#     self.right = None
# def LongestPathWithSameValue(self, A, E):
#   # write your code here
#   def recurse(root, plabel, mxp):
#     if root is None:
#       return 0
#     pl = 1
#     lef = recurse(root.left, root.label, mxp)
#     rig = recurse(root.right, root.label, mxp)
#     mxp[0] = max(mxp[0], pl + lef + rig - 1)
#     if root.label == plabel:
#       return pl + max(lef, rig)
#     return 0

#   nodes = []
#   size = len(A)
#   chils = set(range(1, size + 1))
#   for i, a in enumerate(A):
#     nodes.append(TNode(i + 1, a))
#   for i in range(size - 1):
#     p = E[2 * i]
#     c = E[2 * i + 1]
#     if nodes[p - 1].left is None:
#       nodes[p - 1].left = nodes[c - 1]
#     else:
#       nodes[p - 1].right = nodes[c - 1]
#     if c in chils:
#       chils.remove(c)
#   root = nodes[chils.pop() - 1]
#   mxp = [0]
#   recurse(root, None, mxp)
#   return mxp[0]

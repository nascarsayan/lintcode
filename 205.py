"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
  """
  @param A: An integer array
  @param queries: An query list
  @return: The result list
  """

  def intervalMinNumber(self, A, queries):
    # write your code here
    class SegTNode:

      def __init__(self, st, fl, mn, left=None, right=None):
        self.st, self.fl, self.mn, self.left, self.right = st, fl, mn, left, right

    def makeseg(st, fl):
      root = SegTNode(st, fl, A[st])
      if st == fl:
        return root
      mid = (st + fl) // 2
      root.left, root.right = makeseg(st, mid), makeseg(mid + 1, fl)
      root.mn = min(root.left.mn, root.right.mn)
      return root

    def getmin(root, st, fl):
      if st <= root.st <= root.fl <= fl:
        return root.mn
      if max(st, root.st) > min(fl, root.fl):
        return float('inf')
      return min(getmin(root.left, st, fl), getmin(root.right, st, fl))

    size = len(A)
    if size == 0:
      return [None] * len(queries)
    segt = makeseg(0, size - 1)
    res = []
    for query in queries:
      st, fl = query.start, query.end
      if st > fl:
        res.append(None)
      else:
        res.append(getmin(segt, st, fl))
    return res

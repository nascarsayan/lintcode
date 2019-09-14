"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
  """
  @param A: An integer list
  @param queries: An query list
  @return: The result list
  """

  def intervalSum(self, A, queries):
    # write your code here
    for i in range(1, len(A)):
      A[i] += A[i - 1]
    res = []
    for q in queries:
      st, fl = q.start, q.end
      v = A[fl]
      if st > 0:
        v -= A[st - 1]
      res.append(v)
    return res

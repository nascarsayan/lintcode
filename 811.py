class Solution:
  """
  @param start: the start
  @param end: the end
  @return: is there exists a sequence of moves to transform one string to the other
  """

  def canTransform(self, start, end):
    # Write your code here
    lc, rc = 0, 0
    size, size1 = len(start), len(end)
    if size != size1:
      return False
    for i in range(size):
      if end[i] == 'L':
        lc += 1
      if start[i] == 'R':
        rc += 1
      if start[i] == 'L':
        lc -= 1
      if end[i] == 'R':
        rc -= 1
      if not ((lc >= 0 and rc == 0) or (rc >= 0 and lc == 0)):
        return False
    return (lc == 0 and rc == 0)


print(Solution().canTransform("XRXLXLLRRXRXRRX", "XLRXRLXRRLXXRRX"))

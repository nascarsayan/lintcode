import bisect


class Solution:
  """
  @param m: m pillars of your temple.
  @param woods: length of n different wood
  @return: return the maximum height of the temple.
  """

  def buildTemple(self, m, woods):
    # write your code here.
    def feas(idx, size, woodlen):
      if size - idx >= m:
        return True
      chunks = 0
      for i in range(idx, size):
        chunks += woods[i] // woodlen
        if chunks >= m:
          return True
      return False

    size = len(woods)
    woods.sort()
    mx = 0
    st, fl = 1, woods[size - 1]
    while (st <= fl):
      mid = (st + fl) // 2
      imid = bisect.bisect_left(woods, mid)
      if feas(imid, size, mid):
        mx = max(mx, mid)
        st = mid + 1
      else:
        fl = mid - 1
    return mx


print(Solution().buildTemple(5, [1, 1, 1, 1, 1, 2, 2, 2]))

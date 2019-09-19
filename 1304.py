class Solution:
  """
  @param citations: a list of integers
  @return: return a integer
  """

  def hIndex(self, citations):
    # write your code here
    size = len(citations)
    hdp = [0] * (size + 1)
    for i in range(size):
      hdp[min(size, citations[i])] += 1
    rt = hdp[:]
    for i in range(size)[::-1]:
      rt[i] += rt[i + 1]
    for h in range(size + 1)[::-1]:
      if rt[h] >= h:
        return h
    return None


print(Solution().hIndex([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]))

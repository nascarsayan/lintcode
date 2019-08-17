class Solution:
  """
  @param strs: List[str]
  @return: return an integer
  """

  def findLUSlength(self, strs):
    # write your code here
    def isSub(w1, w2):
      i = 0
      if len(w2) < len(w1):
        return False
      for c in w2:
        if i == len(w1):
          return True
        if w1[i] == c:
          i += 1
      return i == len(w1)

    strs.sort(key=len, reverse=True)
    size = len(strs)
    for i in range(size):
      if all(not isSub(strs[i], strs[j]) for j in range(size) if i != j):
        return len(strs[i])
    return -1


print(Solution().findLUSlength(['aaa', 'acb']))

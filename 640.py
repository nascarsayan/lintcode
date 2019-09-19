class Solution:
  """
  @param s: a string
  @param t: a string
  @return: true if they are both one edit distance apart or false
  """

  def isOneEditDistance(self, s, t):
    # write your code here
    ls, lt = len(s), len(t)
    if abs(ls - lt) > 1:
      return False
    if ls == lt:
      dif = 0
      for i in range(ls):
        if s[i] != t[i]:
          dif += 1
          if dif == 2:
            return False
      if dif == 1:
        return True
      return False
    if ls < lt:
      s, t, ls, lt = t, s, lt, ls
    ds = 0
    for i in range(lt):
      if s[i + ds] != t[i]:
        ds += 1
        if ds == 2:
          return False
    return True


print(Solution().isOneEditDistance('ab', 'aba'))

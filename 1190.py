from functools import cmp_to_key


class Solution:
  """
    @param s: a string
    @param d: List[str]
    @return: return a string
    """

  def findLongestWord(self, s, d):
    # write your code  here
    def isSubst(w1, w2):
      if len(w1) > len(w2):
        return False
      i = 0
      for c in w2:
        if i == len(w1):
          return True
        if w1[i] == c:
          i += 1
      return i == len(w1)

    def mycmp(w1, w2):
      l1 = len(w1)
      l2 = len(w2)
      if l1 != l2:
        return l2 - l1
      return (1, -1)[w1 < w2]

    d.sort(key=cmp_to_key(mycmp))
    for wd in d:
      if isSubst(wd, s):
        return wd
    return ''

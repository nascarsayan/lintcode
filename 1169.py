from collections import Counter


class Solution:
  """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """

  def checkInclusion(self, s1, s2):
    # write your code here
    cnt = Counter(s1)
    size = len(s2)
    i = 0
    tcnt = cnt.copy()
    locc = {}
    tbm = len(s1)
    while (i < size):

      if s2[i] in cnt:
        if tcnt[s2[i]] == 0:
          i = locc[s2[i]] + 1
          tcnt = cnt.copy()
          locc = {}
          tbm = len(s1)
        else:
          tbm -= 1
          if tbm == 0:
            return True
          tcnt[s2[i]] -= 1
          if s2[i] not in locc:
            locc[s2[i]] = i
          i += 1
      else:
        tcnt = cnt.copy()
        tbm = len(s1)
        locc = {}
        i += 1
    return False

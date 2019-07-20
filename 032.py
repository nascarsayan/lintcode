from collections import defaultdict
from copy import deepcopy


class Solution:
  """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

  def minWindow(self, source, target):
    # write your code here
    if (len(source) == 0 or len(target) == 0):
      return ""
    cnt = defaultdict(int)
    for c in target:
      cnt[c] += 1
    ls = len(source)
    lt = len(target)
    minsts = 0
    minwin = ls + 1
    tcnt = deepcopy(cnt)
    nmat = 0
    for idxs in range(ls):
      cs = source[idxs]
      if cs in cnt:
        cnt[cs] -= 1
        if (cnt[cs] >= 0):
          nmat += 1
        if (nmat == lt):
          sts = minsts
          tcnt = deepcopy(cnt)
          for sts in range(minsts, idxs + 1):
            tcs = source[sts]
            if (tcs in cnt):
              if (tcnt[tcs] == 0):
                break
              tcnt[tcs] += 1
          cwin = idxs - sts + 1
          if (cwin < minwin):
            minwin = cwin
            minsts = sts
            cnt = tcnt
    if minwin <= ls:
      return source[minsts:minsts + minwin]
    return ""


# print(Solution().minWindow('adobecodebanc', 'abc'))
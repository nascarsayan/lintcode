from collections import defaultdict
import bisect


class Solution:
  """
  @param: : A string
  @param: : A set of word
  @return: the number of possible sentences.
  """

  def wordBreak3(self, s, dic):
    # Write your code here
    if s == '' or len(dic) == 0:
      return 0
    s = s.lower()
    size = len(s)
    wds = defaultdict(set)
    for wd in dic:
      if wd != '':
        wds[len(wd)].add(wd.lower())
    lns = list(sorted(wds.keys()))
    if lns == 0:
      return 0
    dp = [0] * size
    brks = []
    for fl in range(size):
      if fl + 1 in wds and s[:fl + 1] in wds[fl + 1]:
        dp[fl] += 1
      sti = bisect.bisect_left(brks, fl - lns[-1])
      for st in brks[sti:]:
        if fl - st in wds and s[st + 1:fl + 1] in wds[fl - st]:
          dp[fl] += dp[st]
      if dp[fl] > 0:
        brks.append(fl)
    return dp[-1]


print(Solution().wordBreak3(
    'CatMat', ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]))

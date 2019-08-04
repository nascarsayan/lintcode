class Solution:
  """
  @param: s: A string
  @param: wordDict: A set of words.
  @return: All possible sentences.
  """

  def wordBreak(self, s, wordDict):
    # write your code here
    ls = len(s)
    dp = [[] for _ in range(ls + 1)]
    matched = []
    for st in range(ls - 1, -1, -1):
      bk = False
      if s[st:] in wordDict:
        dp[st].append([[st, ls]])
        bk = True
      for fl in matched:
        if s[st:fl] in wordDict:
          dp[st].extend([[[st, fl]] + x for x in dp[fl]])
          bk = True
      if bk:
        matched.insert(0, st)
    return [' '.join(list(map(lambda x: s[x[0]:x[1]], cut))) for cut in dp[0]]


# print(Solution().wordBreak("lintcode", ["de", "ding", "co", "code", "lint"]))
# !TLE Zindabad

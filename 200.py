class Solution:
  """
    @param s: input string
    @return: the longest palindromic substring
    """

  def spread(self, s, l, lt, rt):
    if lt < 0 or rt >= l:
      return 0, 1
    while (lt >= 0 and rt < l and s[lt] == s[rt]):
      lt -= 1
      rt += 1
    return lt + 1, rt - lt - 1

  def longestPalindrome(self, s):
    # write your code here
    l = len(s)
    maxst = 0
    maxlen = 1
    if len(s) == 2 and s[0] == s[1]:
      return s
    for idx in range(l):
      st1, pl1 = self.spread(s, l, idx, idx)
      st2, pl2 = self.spread(s, l, idx - 1, idx)
      if pl1 > maxlen:
        maxst = st1
        maxlen = pl1
      if pl2 > maxlen:
        maxst = st2
        maxlen = pl2
    return s[maxst:maxst + maxlen]


# print(Solution().longestPalindrome('bb'))
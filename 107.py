class Solution:
  """
    @param: s: A string
    @param: dic: A dictionary of words dict
    @return: A boolean
    """

  def wordBreak(self, s, dic):
    # write your code here
    ls = len(s)
    c = 0
    dp = [False] * ls + [True]
    matched = []
    for st in range(ls - 1, -1, -1):
      if s[st:] in dic:
        dp[st] = True
        matched.insert(0, st)
        continue
      for fl in matched:
        c += 1
        if s[st:fl] in dic:
          dp[st] = True
          matched.insert(0, st)
          break
    print(c)
    return dp[0]


# class Solution:

#   def wordBreak(self, s, wordDict):
#     """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#     n = len(s)
#     wordDict = set(wordDict)

#     dp = [False] * (n + 1)
#     dp[0] = True

#     for i in range(1, n + 1):
#       if s[0:i] in wordDict:
#         dp[i] = True
#         continue
#       for j in range(1, i):
#         if dp[j]:
#           if s[j:i] in wordDict:
#             dp[i] = True
#             break
#     return dp[-1]

# Bad recursive soution
# class Solution:
#   """
#     @param: s: A string
#     @param: dic: A dictionary of words dict
#     @return: A boolean
#     """

#   def recurse(self, s, ssize, dic, dicsize, sidx):
#     if (sidx == ssize):
#       return True
#     matched = list(dic)
#     for idx in range(sidx, ssize):
#       midx = 0
#       while (midx < len(matched)):
#         wd = matched[midx]
#         if (len(wd) == idx - sidx + 1):
#           if (wd[idx - sidx] == s[idx] and
#               self.recurse(s, ssize, dic, dicsize, idx + 1)):
#             return True
#           else:
#             matched.remove(wd)
#             midx -= 1
#         elif (idx - sidx >= len(wd) or wd[idx - sidx] != s[idx]):
#           matched.remove(wd)
#           midx -= 1
#         midx += 1
#       if len(matched) == 0:
#         return False
#     return False

#   def wordBreak(self, s, dic):
#     # write your code here
#     if len(s) == 0 and '' in dic:
#       return True
#     for wd in dic:
#       if len(wd) == 0:
#         dic.remove(wd)
#     dicsize = len(dic)
#     ssize = len(s)
#     return self.recurse(s, ssize, dic, dicsize, 0)

# print(Solution().wordBreak('abccab', set(['a', 'c', 'b'])))

# print(Solution().wordBreak('a', set(['b'])))

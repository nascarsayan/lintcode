class Solution:
  """
  @param s: A string
  @return: An integer
  """

  def minCut(self, s):
    # write your code here
    size = len(s)
    pals = [[False] * size for _ in range(size)]
    mc = []
    for idx in range(size + 1):
      mc.append(size - 1 - idx)
    for st in range(size)[::-1]:
      for mid in range(st, size):
        if s[st] == s[mid] and (mid - st < 2 or pals[st + 1][mid - 1]):
          pals[st][mid] = True
          mc[st] = min(mc[st], mc[mid + 1] + 1)
    return mc[0]


print(Solution().minCut('aaabaa'))

# !TLE 1
# def minCut(self, s):
#   # write your code here
#   def ispalin(st):
#     return st == ''.join(reversed(st))

#   size = len(s)
#   dp = [idx for idx in range(size)]
#   for fl in range(1, size):
#     minc = dp[fl - 1] + 1
#     for st in range(fl):
#       if ispalin(s[st:fl + 1]):
#         if st == 0:
#           minc = 0
#         else:
#           minc = min(minc, dp[st - 1] + 1)
#     dp[fl] = minc
#   return dp[-1]

# !TLE 2
# def minCut(self, s):
#     # write your code here
#     size = len(s)
#     dp = defaultdict(lambda: defaultdict(int))
#     for i in range(size):
#       dp[i][i] = 0
#     for leng in range(2, size + 1):
#       for st in range(size - leng + 1):
#         ist = st + 1
#         ifl = max(st + 1, st + leng - 2)
#         if dp[ist][ifl] == 0 and s[st] == s[st + leng - 1]:
#           dp[st][st + leng - 1] = 0
#         else:
#           minv = float('inf')
#           for mid in range(st, st + leng - 1):
#             minv = min(minv, dp[st][mid] + 1 + dp[mid + 1][st + leng - 1])
#           dp[st][st + leng - 1] = minv
#     print(dp)
#     return dp[0][size - 1]

# # !TLE 3

# import json

# class Solution:

#   def ispal(self, s):
#     size = len(s)
#     for i in range((size + 1) // 2):
#       if s[i] != s[size - i - 1]:
#         return False
#     return True

#   def tokey(self, i, j):
#     return json.dumps([i, j])

#   def recurse(self, s, i, j, dp):
#     if i > j:
#       return 0
#     sij = self.tokey(i, j)
#     if sij in dp:
#       return dp[sij]
#     if i == j or self.ispal(s[i:j + 1]):
#       dp[sij] = 0
#       return dp[sij]
#     inf = float('inf')
#     mini = inf
#     for k in range(i, j):
#       sik = self.tokey(i, k)
#       skj = self.tokey(k + 1, j)
#       lmin = rmin = inf
#       if sik in dp:
#         lmin = dp[sik]
#       else:
#         lmin = self.recurse(s, i, k, dp)
#       if skj in dp:
#         rmin = dp[skj]
#       else:
#         rmin = self.recurse(s, k + 1, j, dp)
#       mini = min(mini, lmin + 1 + rmin)
#     dp[sij] = mini
#     return dp[sij]

#   """
#   @param s: A string
#   @return: An integer
#   """

#   def minCut(self, s):
#     # write your code here
#     dp = {}
#     return self.recurse(s, 0, len(s) - 1, dp)

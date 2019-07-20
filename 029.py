from collections import defaultdict

class Solution:
  """
  @param s1: A string
  @param s2: A string
  @param s3: A string
  @return: Determine whether s3 is formed by interleaving of s1 and s2
  """

  def isInterleave(self, s1, s2, s3):
    # write your code here
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if (len(s1) + len(s2) != l3):
      return False
    if (l3 == 0):
      return True
    dp = defaultdict(bool)
    dp[(-1,-1,-1)] = True
    for l in range(1, l3 + 1):
      if (l1 >= l and s1[l - 1] == s3[l - 1]):
        dp[(l - 1, -1)] = True
      if (l2 >= l and s2[l - 1] == s3[l - 1]):
        dp[(-1, l - 1)] = True
      for i in range(1, l):
        ok = False
        if (l1 >= i and s1[i - 1] == s3[l - 1]):
          ok = ok or dp[(i - 2, l - i - 1)]
        if (l2 >= l - i and s2[l - i - 1] == s3[l - 1]):
          ok = ok or dp[(i - 1, l - i - 2)]
        dp[(i - 1, l - i - 1)] = ok
    return dp[(l1 - 1, l2 - 1)]

  # ! NOC
  def isInterleaveCustom(self, s1, s2, s3):
  # write your code here
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if (len(s1) + len(s2) != l3):
      return False
    dp = defaultdict(lambda: defaultdict(bool))
    for i in range(l1 + 1):
      for j in range(l2 + 1):
        if (i==0 and j==0):
          dp[i][j] = True
        elif (i==0 and s2[j-1]==s3[j-1]):
          dp[i][j] = dp[i][j-1]
        elif (j==0 and s1[i-1]==s3[i-1]):
          dp[i][j] = dp[i-1][j]
        elif(s1[i-1]==s3[i+j-1] and s2[j-1]!=s3[i+j-1]):
          dp[i][j] = dp[i-1][j]
        elif (s1[i-1]!=s3[i+j-1] and s2[j-1]==s3[i+j-1]):
          dp[i][j] = dp[i][j-1]
        elif (s1[i-1]==s3[i+j-1] and s2[j-1]==s3[i+j-1]):
          dp[i][j]=(dp[i-1][j] or dp[i][j-1])
    return dp[l1][l2]

print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
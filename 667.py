class Solution:
  """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

  def longestPalindromeSubseq(self, s):
    # write your code here
    size = len(s)
    if size == 0:
      return 0
    dp = {}
    for i in range(size):
      dp[(i, i)] = 1
    for i in range(size - 1):
      dp[(i, i + 1)] = (1, 2)[s[i] == s[i + 1]]
    for csize in range(3, size + 1):
      for i in range(size - csize + 1):
        j = i + csize - 1
        if s[i] == s[j]:
          dp[(i, j)] = dp[(i + 1, j - 1)] + 2
        else:
          dp[(i, j)] = max(dp[(i + 1, j)], dp[(i, j - 1)])
    return dp[(0, size - 1)]


# print(Solution().longestPalindromeSubseq('baabsbdxxca'))

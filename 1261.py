from collections import Counter


class Solution:
  """
  @param s: a string
  @param k: an integer
  @return: return an integer
  """

  def longestSubstring(self, s, k):
    # write your code here
    if len(s) == 0:
      return 0
    ke, v = Counter(s).most_common()[-1]
    if v < k:
      return max(self.longestSubstring(subs, k) for subs in s.split(ke))
    return len(s)


print(Solution().longestSubstring('ababbc', 2))

# !TLE
# def longestSubstring(self, s, k):
#   # write your code here
#   size = len(s)
#   dp = {}
#   if k == 1:
#     return s
#   subs = ''
#   for i in range(size):
#     dp[i] = Counter()
#   for xs in range(size):
#     for i in range(size - xs):
#       dp[i][s[i + xs]] += 1
#       if dp[i].most_common()[-1][1] >= k:
#         subs = s[i:i + xs + 1]
#   return subs

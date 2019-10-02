from collections import Counter


class Solution:
  """
  @param s: A string
  @param k: An integer
  @return: An integer
  """

  def lengthOfLongestSubstringKDistinct(self, s, k):
    # write your code here
    cnt, size, uniq, mx, st = Counter(), len(s), 0, 0, 0
    if size == 0 or k == 0:
      return 0
    for fl in range(size):
      cnt[s[fl]] += 1
      if cnt[s[fl]] == 1:
        uniq += 1
      while (uniq > k):
        cnt[s[st]] -= 1
        if cnt[s[st]] == 0:
          uniq -= 1
        st += 1
      mx = max(mx, fl - st + 1)
    return mx


print(Solution().lengthOfLongestSubstringKDistinct("WORLD", 4))

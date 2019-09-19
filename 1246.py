from collections import Counter


class Solution:
  """
  @param s: a string
  @param k: a integer
  @return: return a integer
  """

  def characterReplacement(self, s, k):
    # write your code here
    size = len(s)
    cnt = Counter()
    st, mx = 0, 0
    for fl in range(size):
      cnt[s[fl]] += 1
      while (fl - st + 1 - cnt[s[st]] > k):
        cnt[s[st]] -= 1
        st += 1
      mx = max(mx, fl - st + 1)
    return mx


print(Solution().characterReplacement("AAABBBBBBA", 2))

from collections import Counter


class Solution:
  """
  @param s: a string
  @param k: an integer
  @return: the number of substrings there are that contain at least k distinct characters
  """

  def kDistinctCharacters(self, s, k):
    # Write your code here
    cnt = Counter()
    size = len(s)
    if k == 0:
      return int(pow(2, size))
    j = 0
    tot = 0
    for i in range(size):
      cnt[s[i]] += 1
      while (len(cnt) >= k):
        ch = s[j]
        if len(cnt) == k and cnt[ch] == 1:
          break
        cnt[ch] -= 1
        if cnt[ch] == 0:
          cnt.pop(ch)
        j += 1
      if len(cnt) >= k:
        tot += (j + 1)

    return tot


print(Solution().kDistinctCharacters("abcabcabcabc", 3))

from functools import cmp_to_key


class Solution:
  """
  @param dic: a dictionary
  @param s: a string
  @return: the longest one existed in the given dictionary
  """

  def longestSubsequence(self, dic, s):
    # Write your code here
    def mycmp(x, y):
      c1 = len(x) - len(y)
      if c1 != 0:
        return -c1
      return (1, -1)[x < y]

    dic = list(sorted(dic, key=cmp_to_key(mycmp)))
    ss = len(s)
    for wd in dic:
      idxs, idxw, swd = 0, 0, len(wd)
      while (idxs < ss and idxw < swd):
        if wd[idxw] == s[idxs]:
          idxw += 1
        idxs += 1
      if idxw == swd:
        return wd
    return ''


print(Solution().longestSubsequence(["de", "ding", "co", "code", "lint"],
                                    "lintcode"))

from collections import Counter


class Solution:
  """
  @param s: the given string
  @return: all the palindromic permutations (without duplicates) of it
  """

  def generatePalindromes(self, s):
    # write your code here
    def recurse(idx, path):
      if idx == size // 2:
        res.append(path + odd + path[::-1])
      for k in chars:
        if cnt[k] > 0:
          cnt[k] -= 1
          recurse(idx + 1, path + k)
          cnt[k] += 1

    size = len(s)
    cnt, odd = Counter(s), ''
    chars = list(sorted(list(cnt.keys())))
    for k in chars:
      if cnt[k] % 2 == 1:
        if odd != '':
          return []
        odd = k
      cnt[k] = cnt[k] // 2
    res = []
    recurse(0, '')
    return res


print(Solution().generatePalindromes('aaabbbbcc'))

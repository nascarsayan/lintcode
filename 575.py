class Solution:
  """
  @param s: an expression includes numbers, letters and brackets
  @return: a string
  """

  def expressionExpand(self, s):
    # write your code here
    size = len(s)
    if size == 0:
      return s
    stac, s2, times = '', '', ''
    i, bopen = 0, 0
    while (i < size):
      c = s[i]
      if '0' <= c <= '9' and bopen == 0:
        times += c
      elif c == '[':
        stac += c
        bopen += 1
      elif c == ']':
        stac += c
        bopen -= 1
        if bopen == 0:
          s2 += self.expressionExpand(stac[1:-1]) * int(times)
          stac = ''
          times = ''
      elif len(stac) == 0:
        s2 += c
      else:
        stac += c
      i += 1
    return s2


print(Solution().expressionExpand("3[2[ad]3[pf]]xyz"))

NG = 4


class Solution:

  def recurse(self, s, curr, permut):
    ssize = len(s)
    csize = len(curr)
    if (csize == 3):
      num = int(s)
      if num < 256 and (str(num) == s):
        permut.append(curr + [s])
      return
    if (ssize < NG - csize):
      return
    for i in range(1, min(4, ssize - (NG - csize - 2))):
      nstr = s[:i]
      num = int(nstr)
      if num < 256 and (str(num) == nstr):
        self.recurse(s[i:], curr + [nstr], permut)

  """
  @param s: the IP string
  @return: All possible valid IP addresses
  """

  def restoreIpAddresses(self, s):
    # write your code here
    size = len(s)
    permut = []
    if size < 4 or size > 12:
      return permut
    self.recurse(s, [], permut)
    return ['.'.join(x) for x in permut]


# print(Solution().restoreIpAddresses('010010'))

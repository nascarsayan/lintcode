class Solution:
  """
    @param s: Roman representation
    @return: an integer
    """

  def romanToInt(self, s):
    # write your code here
    l = len(s)
    valmap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    tot = 0
    for i in range(l - 1):
      if valmap[s[i]] < valmap[s[i + 1]]:
        tot -= valmap[s[i]]
      else:
        tot += valmap[s[i]]
    return tot + valmap[s[-1]]


# print(Solution().romanToInt('XCIX'))
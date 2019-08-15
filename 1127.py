class Solution:
  """
    @param s: a string
    @param dict: a list of strings
    @return: return a string
    """

  def addBoldTag(self, s, dct):
    # write your code here
    szs = len(s)
    dctl = sorted(list(dct), key=lambda x: len(x))
    szdct = len(dctl)
    if szdct == 0 or szs == 0:
      return s
    ints = []
    offs = len(dctl[0])
    for st in range(szs - offs + 1):
      cs = s[st:]
      for wd in dctl:
        if cs.startswith(wd):
          cfl = min(szs, st + len(wd))
          if len(ints) == 0:
            ints.append([st, cfl])
          else:
            lastfl = ints[-1][1]
            if lastfl >= st:
              ints[-1][1] = max(lastfl, cfl)
            else:
              ints.append([st, cfl])
    szints = len(ints)
    if szints == 0:
      return s
    rets = s[:ints[0][0]]
    for i in range(szints - 1):
      rets = (
          rets + '<b>' + s[ints[i][0]:ints[i][1]] + '</b>' +
          s[ints[i][1]:ints[i + 1][0]])
    rets = (
        rets + '<b>' + s[ints[szints - 1][0]:ints[szints - 1][1]] + '</b>' +
        s[ints[szints - 1][1]:])
    return rets

class Solution:

  def ambiguousCoordinates(self, S):
    dpw = {}
    dpf = {}
    dpc = {}

    def isWhole(s):
      if len(s) == 0:
        return False
      if s in dpw:
        return dpw[s]
      dpw[s] = str(int(s)) == s
      return dpw[s]

    def isFrac(s):
      if len(s) == 0:
        return True
      if s in dpf:
        return dpf[s]
      if s[-1] == '0':
        dpf[s] = False
      else:
        dpf[s] = True
      return dpf[s]

    def getValids(coord):
      if coord in dpc:
        return dpc[coord]
      size = len(coord)
      poss = []
      for i in range(1, size):
        if isWhole(coord[:i]) and isFrac(coord[i:]):
          poss.append(coord[:i] + '.' + coord[i:])
      if isWhole(coord):
        poss.append(coord)
      dpc[coord] = poss
      return dpc[coord]

    S = S[1:-1]
    res = []
    for i in range(len(S)):
      xcoo = getValids(S[:i])
      if len(xcoo) > 0:
        ycoo = getValids(S[i:])
        for iy in ycoo:
          for ix in xcoo:
            res.append('({}, {})'.format(ix, iy))
    return res


print(Solution().ambiguousCoordinates("(00011)"))

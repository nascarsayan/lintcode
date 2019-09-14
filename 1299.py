from collections import Counter


class Solution:

  def getHint(self, secret, guess):
    bul, cow = 0, 0
    nms, nmg = '', ''
    for cs, cg in zip(secret, guess):
      if cs == cg:
        bul += 1
      else:
        nms += cs
        nmg += cg
    cnts, cntg = Counter(nms), Counter(nmg)
    for mc in set(cnts.keys()).intersection(set(cntg.keys())):
      cow += min(cnts[mc], cntg[mc])
    return '{}A{}B'.format(bul, cow)

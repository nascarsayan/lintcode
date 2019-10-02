from collections import Counter


class Solution:
  """
  @param s: a string
  @return: return a string
  """

  def originalDigits(self, s):
    # write  your code here
    ccnt = Counter(s)
    dcnt = [0] * 10
    topo = [(0, 'zero', 'z'), (2, 'two', 'w'), (4, 'four', 'u'),
            (6, 'six', 'x'), (8, 'eight', 'g'), (1, 'one', 'o'),
            (3, 'three', 't'), (5, 'five', 'f'), (7, 'seven', 's'),
            (9, 'nine', 'i')]
    for dig, wd, dist in topo:
      dcnt[dig] = ccnt[dist]
      for c in wd:
        ccnt[c] -= dcnt[dig]
    res = ''
    for i, v in enumerate(dcnt):
      res += str(i) * v
    return res


print(Solution().originalDigits("fviefuro"))

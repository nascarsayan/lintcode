from collections import Counter


class Solution:
  """
  @param S: a string
  @return: return a string
  """

  def reorganizeString(self, S):
    # write your code here
    size = len(S)
    sls = []
    reas = ''
    cnts = Counter(S).most_common()
    if cnts[0][1] > (size + 1) // 2:
      return reas
    for cnt in cnts:
      sls.extend([cnt[0]] * cnt[1])
    st, fl = 0, size - 1
    while (st <= fl):
      reas += sls[st]
      st += 1
      if (st <= fl):
        reas += sls[fl]
      fl -= 1
    return reas

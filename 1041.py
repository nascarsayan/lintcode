from collections import Counter


class Solution:
  """
  @param S: a string
  @return: return a string
  """

  def reorganizeString(self, S):
    # write your code here
    size = len(S)
    if size < 2:
      return S
    res = []
    cnts = Counter(S).most_common()
    if cnts[0][1] > (size + 1) // 2:
      return ''
    res.extend([cnts[0][0]] * cnts[0][1])
    pos = 1
    for ch, fr in cnts[1:]:
      for _ in range(fr):
        res.insert(pos, ch)
        pos = (pos + 2) % (len(res) + 1)
    return ''.join(res)


print(Solution().reorganizeString('vvvlox'))

from collections import Counter


class Solution:
  """
  @param s: a string
  @return: return List[str]
  """

  def findRepeatedDnaSequences(self, s):
    # write your code here
    size = len(s)
    cnt = Counter()
    rep = []
    for i in range(size - 9):
      cnt[s[i:i + 10]] += 1
    for seq in cnt:
      if cnt[seq] > 1:
        rep.append(seq)
    return rep

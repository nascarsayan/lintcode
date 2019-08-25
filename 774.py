# from collections import Counter


class Solution:
  """
  @param s: a string represent DNA sequences
  @return: all the 10-letter-long sequences
  """

  def findRepeatedDna(self, s):
    # write your code here
    SQS = 10
    s1 = set()
    s2 = set()
    for idx in range(len(s) - SQS + 1):
      subs = s[idx:idx + 10]
      if subs in s2:
        continue
      if subs in s1:
        s2.add(subs)
      else:
        s1.add(subs)
    return list(s2)

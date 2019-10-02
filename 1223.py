class Solution:
  """
  @param p: the given string
  @return: the number of different non-empty substrings of p in the string s
  """

  def findSubstringInWraproundString(self, p):
    # Write your code here
    q = list(map(lambda x: ord(x) - ord('a'), p))
    if len(q) == 0:
      return 0
    mxs = [0] * 26
    currl = mxs[q[0]] = 1
    for c1, c2 in zip(q, q[1:]):
      currl = currl + 1 if (c2 - c1) % 26 == 1 else 1
      mxs[c2] = max(mxs[c2], currl)
    return sum(mxs)


print(Solution().findSubstringInWraproundString('d'))

class Solution:
  """
  @param S: a string
  @param indexes: the index array
  @param sources: the source array
  @param targets: the target array
  @return: the string after operation
  """

  def findReplaceString(self, S, indexes, sources, targets):
    # Write your code here.
    conv = list(zip(indexes, sources, targets))
    lc = len(conv)
    ls = len(S)
    if lc == 0 or ls == 0:
      return S
    conv.sort(key=lambda x: x[0])
    parts = []
    pre = 0
    for i, s, t in conv:
      if i >= ls:
        break
      subs = S[i:i + len(s)]
      if subs == s:
        parts.append(S[pre:i])
        parts.append(t)
        pre = i + len(s)
    parts.append(S[pre:])
    return ''.join(parts)


# print(Solution().findReplaceString("abcd", [0, 2], ["a", "cd"],
#                                    ["eee", "ffff"]))

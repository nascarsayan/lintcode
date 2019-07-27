class Solution:
  """
    @param strs: A list of strings
    @return: The longest common prefix
    """

  def longestCommonPrefix(self, strs):
    # write your code here
    nst = len(strs)
    if nst == 0:
      return ''
    maxlcp = min([len(s) for s in strs])
    if maxlcp == 0:
      return ''
    for lcp in range(maxlcp):
      ok = True
      for s in strs[1:]:
        if strs[0][lcp] != s[lcp]:
          ok = False
          break
      if not ok:
        return strs[0][:lcp]
    return strs[0][:maxlcp]


# print(Solution().longestCommonPrefix(['ABCDEFG', 'ABCEFG', 'ABCEFA']))
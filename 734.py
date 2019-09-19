class Solution:
  """
  @param source: the input string
  @return: the number of subsequences
  """

  def countSubsequences(self, source):
    # write your code here
    ac, bc, cc = 0, 0, 0
    for ch in source:
      if ch == 'a':
        ac = (ac << 1) + 1
      elif ch == 'b':
        bc = (bc << 1) + ac
      elif ch == 'c':
        cc = (cc << 1) + bc
    return cc


print(Solution().countSubsequences('abbc'))

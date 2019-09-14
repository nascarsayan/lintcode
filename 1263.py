class Solution:
  """
  @param s: the given string s
  @param t: the given string t
  @return: check if s is subsequence of t
  """

  def isSubsequence(self, s, t):
    # Write your code here
    ssz = len(s)
    if ssz == 0:
      return True
    ptr = 0
    for c in t:
      if c == s[ptr]:
        ptr += 1
        if ptr == ssz:
          return True
    return False

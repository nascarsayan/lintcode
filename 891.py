class Solution:
  """
  @param s: a string
  @return bool: whether you can make s a palindrome by deleting at most one character
  """

  def validPalindrome(self, s):
    # Write your code here
    def isPalin(st, fl):
      while (st < fl and s[st] == s[fl]):
        st += 1
        fl -= 1
      return st >= fl

    size = len(s)
    st, fl = 0, size - 1
    while (st < fl and s[st] == s[fl]):
      st += 1
      fl -= 1
    if st == fl:
      return True
    return isPalin(st + 1, fl) or isPalin(st, fl - 1)

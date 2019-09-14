# https://www.lintcode.com/problem/rotate-string/


class Solution:
  """
  @param str: An array of char
  @param offset: An integer
  @return: nothing
  """

  def rotateString(self, s, offset):
    # write your code here
    return s[-offset:] + s[:-offset]


print(Solution().rotateString('abcdefg', 3))

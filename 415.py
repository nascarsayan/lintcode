class Solution:
  """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

  def isPalindrome(self, s):
    # write your code here
    def isAlNum(x):
      o = ord(x)
      if (o >= 48 and o <= 57) or (o >= 97 and o <= 122):
        return True
      return False

    s = list(filter(isAlNum, list(map(lambda x: x.lower(), s))))
    size = len(s)
    for idx in range((size + 1) // 2):
      if s[idx] != s[size - idx - 1]:
        return False
    return True


# print(Solution().isPalindrome('A man, a plan, a canal: Panama'))

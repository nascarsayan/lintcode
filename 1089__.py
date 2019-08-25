class Solution:
  """
  @param s: the given string
  @return: whether this string is valid
  """

  def checkValidString(self, s):
    # Write your code here
    size = len(s)

    def recurse(idx, v):
      if v < 0:
        return False
      if idx == size:
        return v == 0
      if s[idx] != '*':
        return recurse(idx + 1, v + (-1, 1)[s[idx] == '('])
      if recurse(idx + 1, v + 1):
        return True
      if recurse(idx + 1, v):
        return True
      return recurse(idx + 1, v - 1)

    return recurse(0, 0)


print(Solution().checkValidString(
    "(****)()*((())(*)))((**()))()(**()*((*((*()(((*)((()***)(()(()))*****((()()(***"
))

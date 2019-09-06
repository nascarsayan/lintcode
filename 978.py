class Solution:
  """
  @param s: the given expression
  @return: the result of expression
  """

  def calculate(self, s):
    # Write your code here
    s = '(' + s + ')'
    i = len(s) - 1
    while (i >= 0):
      if s[i] == '(':
        ex = ''
        if s[i + 1] not in '+-':
          ex += '+'
        s = s[:i + 1] + ex + s[i + 1:]
      i -= 1
    i = len(s) - 1
    while (i >= 0):
      if s[i] == ' ':
        s = s[:i] + s[i + 1:]
      i -= 1
    size = len(s)
    stac = []
    i = 0
    while (i < size):
      if len(stac) > 0 and type(stac[-1]) is int and s[i].isdigit():
        stac[-1] = stac[-1] * 10 + int(s[i])
      elif s[i].isdigit():
        stac.append(int(s[i]))
      else:
        stac.append(s[i])
      if stac[-1] == ')':
        tot = 0
        stac.pop(-1)
        while (stac[-1] != '('):
          v = stac.pop(-1)
          op = stac.pop(-1)
          if op == '+':
            tot += v
          else:
            tot -= v
        stac.pop(-1)
        sgn = ('-', '+')[tot >= 0]
        if len(stac) > 0 and stac[-1] in '+-':
          stac[-1] = ('-', '+')[eval(sgn + '1') * eval(stac[-1] + '1') > 0]
        else:
          stac.append(('-', '+')[tot >= 0])
        stac.append(abs(tot))
        # print(stac)
      i += 1
    return eval(stac[0] + str(stac[1]))


print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))

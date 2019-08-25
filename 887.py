class Solution:
  """
  @param expression: a string, denote the ternary expression
  @return: a string
  """

  def parseTernary(self, expression):
    # write your code here
    size = len(expression)
    st, fl = 0, size - 1
    while (st < fl):
      op, idx = 1, st + 2
      while (op > 0):
        if expression[idx] == '?':
          op += 1
        elif expression[idx] == ':':
          op -= 1
        idx += 1
      if expression[st] == 'T':
        st += 2
        fl = idx - 2
      else:
        st = idx
    return expression[st]


print(Solution().parseTernary("F?1:T?3:1"))

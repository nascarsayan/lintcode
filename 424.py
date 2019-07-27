import math


class Solution:
  """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """

  def evalRPN(self, tokens):
    # write your code here
    stac = []
    try:
      for token in tokens:
        if (ord(token[-1]) >= 48 and ord(token[-1]) < 58):
          stac.append(int(token))
        else:
          v2 = stac.pop(-1)
          v1 = stac.pop(-1)
          v = 0
          if token == '+':
            v = v1 + v2
          elif token == '-':
            v = v1 - v2
          elif token == '*':
            v = v1 * v2
          elif token == '/':
            v = int(math.copysign((abs(v1) // abs(v2)), v1 / v2))
          else:
            return None
          stac.append(v)
          # print('%d %s %d = %d' % (v1, token, v2, v))
      v = stac.pop()
      if len(stac) > 0:
        return None
      return v
    except Exception as e:
      print(e)
      return None


# print(Solution().evalRPN(["4", "13", "5", "/", "+"]))

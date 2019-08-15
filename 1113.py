class Solution:
  """
    @param equation: a string
    @return: return a string
    """

  def solveEquation(self, equation):
    # write your code here
    lx, lv, rx, rv = 0, 0, 0, 0
    eqi = equation.find('=')
    if not 0 < eqi < len(equation) - 1:
      return 'Invalid equation'
    equation += '='
    coeff = ''
    for idx in range(eqi + 1):
      c = equation[idx]
      if c in ['+', '-', '='] and len(coeff) > 0:
        if coeff[-1] == 'x':
          v = coeff[:-1]
          if len(v) == 0 or not ('0' <= v[-1] <= '9'):
            v += '1'
          lx += int(v)
        else:
          lv += int(coeff)
        coeff = ''
      coeff += c
    coeff = ''
    for idx in range(eqi + 1, len(equation)):
      c = equation[idx]
      if c in ['+', '-', '='] and len(coeff) > 0:
        if coeff[-1] == 'x':
          v = coeff[:-1]
          if len(v) == 0 or not ('0' <= v[-1] <= '9'):
            v += '1'
          rx += int(v)
        else:
          rv += int(coeff)
        coeff = ''
      coeff += c
    tx = lx - rx
    tv = rv - lv
    if tx == 0:
      if tv == 0:
        return 'Infinite solutions'
      else:
        return 'No solution'
    else:
      return 'x=%d' % (tv // tx)


print(Solution().solveEquation('x+5-3+x=6+x-2'))

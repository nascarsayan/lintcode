class Solution:
  """
  @param expression: a string
  @return: return a string
  """

  def fractionAddition(self, expression):
    # write your code here
    def gcd(v1, v2):
      while (v1 > 0):
        v1, v2 = v2 % v1, v1
      return v2

    size = len(expression)
    if size == 0:
      return expression
    if expression[0] not in '+-':
      expression = '+' + expression
    expression = expression.replace('+', ' +').replace('-', ' -')
    fracs = expression.split(' ')[1:]
    nums, dens = [], []
    for frac in fracs:
      num, den = frac.split('/')
      nums.append(eval(num))
      dens.append(eval(den))
    resden = 1
    for den in dens:
      resden *= den
    resnum = 0
    for num, den in zip(nums, dens):
      resnum += (resden // den) * num
    hcf = gcd(abs(resnum), resden)
    resnum //= hcf
    resden //= hcf
    return '%d/%d' % (resnum, resden)


print(Solution().fractionAddition('1/3-1/2'))

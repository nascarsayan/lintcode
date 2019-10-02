import re
import operator


class Solution:
  """
  @param inp: a string
  @return: return List[int]
  """

  def diffWaysToCompute(self, inp):
    # write your code here
    dp = {}
    s2o = {'+': operator.add, '-': operator.sub, '*': operator.mul}

    def recurse(st, fl, ist, ifl):
      if ist > ifl:
        return [int(inp[st:fl + 1])]
      if (st, fl) in dp:
        return dp[(st, fl)]
      res = []
      for imid in range(ist, ifl + 1):
        larr = recurse(st, ops[imid] - 1, ist, imid - 1)
        rarr = recurse(ops[imid] + 1, fl, imid + 1, ifl)
        res.extend([s2o[inp[ops[imid]]](x, y) for x in larr for y in rarr])
      dp[(st, fl)] = res
      return dp[(st, fl)]

    size = len(inp)
    res = []
    if size == 0:
      return res
    if inp[0] == '-':
      inp = '0' + inp
      size += 1
    ops = list(map(lambda x: x.start(), re.finditer(r'[+*-]', inp)))
    return recurse(0, size - 1, 0, len(ops) - 1)


print(Solution().diffWaysToCompute('2-3*4'))

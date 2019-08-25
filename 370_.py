class Solution:
  """
  @param expression: A string array
  @return: The Reverse Polish notation of this expression
  """

  def convertToRPN(self, expression):
    # write your code here
    prece = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0}
    nds = []
    tors = []
    for part in expression:
      if part.isdigit():
        nds.append([part])
      else:
        tors.append(part)
    while()
        cond = ('len(tors) > 0 and prece[tors[-1]] >= prece[tors[-2]]',
                'tors[-1] != "("')[part == ')']
        if part != ')':
          tors.append(part)
        while (eval(cond)):
          op2 = nds.pop(-1)
          op1 = nds.pop(-1)
          op = tors.pop(-1)
          nds.append(op1 + op2 + [op])
      print(nds, tors)
    if len(tors) == 1:
      op2 = nds.pop(-1)
      op1 = nds.pop(-1)
      op = tors.pop(-1)
      nds.append(op1 + op2 + [op])
    return nds[0]


print(Solution().convertToRPN(["3", "+", "4", "*", "5"]))

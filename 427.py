# https://www.lintcode.com/problem/generate-parentheses/
class Solution:

  def recurse(self, n, op, ed, curr, permuts):
    if (op > n or ed > op):
      return
    if (op == n and ed == n):
      permuts.append(curr)
      return
    self.recurse(n, op + 1, ed, curr + '(', permuts)
    self.recurse(n, op, ed + 1, curr + ')', permuts)

  """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

  def generateParenthesis(self, n):
    # write your code here
    permuts = []
    self.recurse(n, 0, 0, '', permuts)
    return permuts


# print(Solution().generateParenthesis(3))
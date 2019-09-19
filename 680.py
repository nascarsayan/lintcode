class Solution:
  """
    @param: : a string to be split
    @return: all possible split string array
    """

  def splitString(self, s):
    # write your code here
    size = len(s)
    if size == 0:
      return [[]]
    if size == 1:
      return [[s]]
    dp1, dp2 = [[s[0]]], [[s[0], s[1]], [s[:2]]]
    for i in range(2, size):
      dp1, dp2 = dp2, ([x + [s[i]] for x in dp2] +
                       [x + [s[i - 1:i + 1]] for x in dp1])
    return dp2


print(Solution().splitString('123'))

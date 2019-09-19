class Solution:
  """
  @param lower: Integer : lower bound
  @param upper: Integer : upper bound
  @return: a list of every possible Digit Divide Numbers
  """

  def digitDivideNums(self, lower, upper):
    # write your code here
    res = []
    for i in range(lower, upper + 1):
      temp = i
      while (temp > 0):
        dig = temp % 10
        if dig == 0 or i % dig != 0:
          break
        temp //= 10
      if temp == 0:
        res.append(i)
    return res


print(Solution().digitDivideNums(1, 22))

class Solution:
  """
  @param n: An integer
  @return: A boolean which equals to true if the first player will win
  """

  def firstWillWin(self, n):
    # write your code here
    if n < 1:
      return False
    w = [True, True]
    for idx in range(n - 2):
      w = [w[1], not (w[0] and w[1])]
    return w[1]

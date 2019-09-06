class Solution:
  """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """

  def canWin(self, s):
    # write your code here
    return any(not self.canWin(s[:i] + '--' + s[i + 2:])
               for i in range(len(s) - 1)
               if s[i:i + 2] == '++')

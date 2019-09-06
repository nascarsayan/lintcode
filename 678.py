class Solution:
  """
  @param stri: String
  @return: String
  """

  def shortestPalindrome(self, stri):
    # Write your code here
    size = len(stri)
    fl = size
    while (stri[:fl] != stri[:fl][::-1]):
      fl -= 1
    return stri[fl:][::-1] + stri

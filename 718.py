import re


class Solution:
  """
  @param A: string A to be repeated
  @param B: string B
  @return: the minimum number of times A has to be repeated
  """

  def repeatedString(self, A, B):
    # write your code here
    if B == '':
      return 0
    if A == '':
      return (-1, 0)[B == '']
    mat = re.search(B, A * ((len(B) // len(A)) + 2))
    if mat is None:
      return -1
    idx = mat.end()
    return (idx + len(A) - 1) // len(A)


print(Solution().repeatedString('abcd', 'cdabcdab'))

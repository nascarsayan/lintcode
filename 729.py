class Solution:
  """
  @param A: the given number
  @param B: another number
  @return: the last digit of B! / A! 
  """

  def computeLastDigit(self, A, B):
    # write your code here
    ld = 1
    for i in range(A + 1, min(A + 10, B + 1)):
      ld = ((i % 10) * ld) % 10
    return ld

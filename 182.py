class Solution:
  """
  @param A: A positive integer which has N digits, A is a string
  @param k: Remove k digits
  @return: A string
  """

  def DeleteDigits(self, A, k):
    # write your code here
    size = len(A)
    if k == 0 or size == 0:
      return A
    if k >= size:
      return ''
    stac = []
    for i in range(size):
      while (stac) and k > 0 and ord(stac[-1]) > ord(A[i]):
        stac.pop(-1)
        k -= 1
      stac.append(A[i])
    while (k > 0):
      stac.pop(-1)
      k -= 1
    return ''.join(stac).lstrip('0')


print(Solution().DeleteDigits('90249', 2))

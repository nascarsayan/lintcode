class Solution:
  """
  @param A: an array
  @return: the number of arithmetic slices in the array A.
  """

  def numberOfArithmeticSlices(self, A):
    # Write your code here
    A.append(float('inf'))
    tot = 0
    curr = 0
    for i in range(2, len(A)):
      if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
        curr += 1
      else:
        tot += (curr * (curr + 1)) // 2
        curr = 0
    return tot

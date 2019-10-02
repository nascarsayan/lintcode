class Solution:
  """
  @param A: the array of A
  @param B: the array of B
  @return: the most advantageous A array after rearrangement
  """

  def advantageCount(self, A, B):
    # write your code here.
    B1 = list(sorted([(v, i) for i, v in enumerate(B)]))
    A.sort()
    size = len(A)
    i = size - 1
    while (i > 0):
      j = i
      while (j > 0 and A[i] <= B1[j][0]):
        j -= 1
      A = A[i - j:i + 1] + A[:i - j] + A[i + 1:]
      i = j - 1

    res = [None] * size
    for i, v in enumerate(A):
      res[B1[i][1]] = v
    return res


print(Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))

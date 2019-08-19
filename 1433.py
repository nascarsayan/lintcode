from collections import Counter


class Solution:
  """
  @param A: the matrix A
  @param B: the matrix B
  @return: maximum possible overlap
  """

  def largestOverlap(self, A, B):
    # Write your code here.
    nr = len(A)
    nc = len(B)
    dif = Counter()
    A1 = []
    B1 = []
    for ir in range(nr):
      for ic in range(nc):
        if A[ir][ic] == 1:
          A1.append((ir, ic))
        if B[ir][ic] == 1:
          B1.append((ir, ic))
    for ai, aj in A1:
      for bi, bj in B1:
        dif[(ai - bi), (aj - bj)] += 1
    return max(dif.values() or [0])


print(Solution().largestOverlap([[0]], [[1]]))

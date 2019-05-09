# https://www.lintcode.com/problem/merge-two-sorted-arrays/

class Solution:
  """
  @param A: sorted integer array A
  @param B: sorted integer array B
  @return: A new sorted integer array
  """
  def mergeSortedArray(self, A, B):
    # write your code here
    ia = 0
    ib = 0
    la = len(A)
    lb = len(B)
    C = []
    while(ia < la and ib < lb):
      if (A[ia] < B[ib]):
        C.append(A[ia])
        ia += 1
      else:
        C.append(B[ib])
        ib += 1
    C = C + A[ia:] + B[ib:]
    return C

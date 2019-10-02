from collections import Counter


class Solution:
  """
  @param A: a list
  @param B: a list
  @param C: a list
  @param D: a list
  @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
  """

  def fourSumCount(self, A, B, C, D):
    # Write your code here
    size = [len(A), len(B), len(C), len(D)]
    cnt = Counter()
    for i1 in range(size[0]):
      for i2 in range(size[1]):
        cnt[A[i1] + B[i2]] += 1
    res = 0
    for i3 in range(size[2]):
      for i4 in range(size[3]):
        res += cnt[-(C[i3] + D[i4])]
    return res

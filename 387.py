class Solution:
  """
  @param A: An integer array
  @param B: An integer array
  @return: Their smallest difference.
  """

  def smallestDifference(self, A, B):
    # write your code here
    la, lb = len(A), len(B)
    if la == 0 or lb == 0:
      return None
    A.sort()
    B.sort()
    pa, pb, mn = 0, 0, float('inf')
    while (pa < la and pb < lb):
      while (pa < la and A[pa] <= B[pb]):
        pa += 1
      if pa > 0:
        mn = min(mn, B[pb] - A[pa - 1])
      if pa == la:
        break
      while (pb < lb and A[pa] >= B[pb]):
        pb += 1
      if pb > 0:
        mn = min(mn, A[pa] - B[pb - 1])
      if mn == 0:
        return mn
    return mn


print(Solution().smallestDifference([1, 2, 3, 4], [7, 6, 5]))

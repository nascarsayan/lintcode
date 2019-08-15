class Solution:
  """
  @param A: the array
  @return: Maximum Sum Circular Subarray
  """

  def maxSubarraySumCircular(self, A):
    tot = 0
    size = len(A)
    mn = float('inf')
    arrs = 0
    for i in range(size):
      arrs += A[i]
      if tot + A[i] > 0:
        tot = 0
        continue
      tot += A[i]
      mn = min(mn, tot)
    mx = arrs - mn
    if mx == 0:
      if 0 not in A:
        mx = float('-inf')
    tot = 0
    for i in range(size):
      tot += A[i]
      mx = max(mx, tot)
      if tot < 0:
        tot = 0
    return mx


print(Solution().maxSubarraySumCircular([-2, -3, -2]))

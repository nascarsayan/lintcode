class Solution:
  """
  @param A: an array
  @return: the sum of subarray minimums
  """

  def sumSubarrayMins(self, A):
    # Write your code here.
    PR = 10**9 + 7
    ninf = float('-inf')
    A = [ninf] + A + [ninf]
    size = len(A)
    tot = 0
    stac = []
    for idx in range(size):
      while stac and A[stac[-1]] > A[idx]:
        j = stac.pop(-1)
        k = stac[-1]
        tot += ((idx - j) * (j - k)) * A[j]
      stac.append(idx)
    return tot % PR


print(Solution().sumSubarrayMins([3, 1, 2, 4]))

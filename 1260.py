class Solution:
  """
  @param A: an array
  @return: the maximum value of F(0), F(1), ..., F(n-1)
  """

  def maxRotateFunction(self, A):
    # Write your code here
    fval, tot = 0, 0
    size = len(A)
    for i, a in enumerate(A):
      fval += i * a
      tot += a
    mx = fval
    for i in range(1, size):
      fl = (i + size - 1) % size
      fval = fval - tot + size * A[fl]
      mx = max(mx, fval)
    return mx


print(Solution().maxRotateFunction([4, 3, 2, 6]))

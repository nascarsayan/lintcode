class Solution:
  """
  @param A: an array
  @param B: an array
  @return: the minimum number of swaps to make both sequences strictly increasing
  """

  def minSwap(self, A, B):
    # Write your code here
    n = 0
    y = 1
    size = len(A)
    inf = float('inf')
    for idx in range(1, size):
      nn = (inf, n)[A[idx] > A[idx - 1] and B[idx] > B[idx - 1]]
      yn = (inf, y)[A[idx] > B[idx - 1] and B[idx] > A[idx - 1]]

      ny = (inf, n + 1)[B[idx] > A[idx - 1] and A[idx] > B[idx - 1]]
      yy = (inf, y + 1)[B[idx] > B[idx - 1] and A[idx] > A[idx - 1]]
      n = min(nn, yn)
      y = min(ny, yy)
    return min(n, y)

import bisect


class Solution:
  """
  @param A: An array of integers
  @return: A long integer
  """

  def permutationIndex(self, A):
    # write your code here
    sa = sorted(A)
    size = len(sa)
    idx = 0
    fac = 1
    for i in range(2, size + 1):
      fac *= i
    for i in range(size):
      fac //= (size - i)
      pos = bisect.bisect_left(sa, A[i])
      idx += pos * fac
      sa.pop(pos)
    return idx + 1


print(Solution().permutationIndex([2, 6, 4, 5, 8, 1, 7, 3]))

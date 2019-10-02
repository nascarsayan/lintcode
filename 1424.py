class Solution:
  """
  @param A:
  @return: the length of the longest mountain
  """

  def longestMountain(self, A):
    # write your code here
    size = len(A)
    locmax = []
    mx = 0
    for i in range(1, size - 1):
      if A[i - 1] < A[i] > A[i + 1]:
        locmax.append(i)
    for mi in locmax:
      st, fl = mi - 1, mi + 1
      while (st >= 0 and A[st] < A[st + 1]):
        st -= 1
      while (fl < size and A[fl] < A[fl - 1]):
        fl += 1
      mx = max(mx, fl - st - 1)
    return mx

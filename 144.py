class Solution:
  """
  @param: A: An integer array.
  @return: nothing
  """

  def rerange(self, A):
    # write your code here
    size = len(A)
    if size < 3:
      return
    negs, sgn = 0, 1
    for i in range(size):
      if A[i] < 0:
        negs += 1
    if negs < (size + 1) // 2:
      sgn = -1
    st, fl = 0, size - 1
    while (st < fl):
      while (st < fl and A[st] * sgn < 0):
        st += 1
      while (st < fl and A[fl] * sgn > 0):
        fl -= 1
      A[st], A[fl] = A[fl], A[st]
      st, fl = st + 1, fl - 1
    mid = (size - 1) // 2
    if size % 2 == 1:
      A[mid], A[-1] = A[-1], A[mid]
      size -= 1
    st, fl = 1, size - 2
    while (st < fl):
      A[st], A[fl] = A[fl], A[st]
      st, fl = st + 2, fl - 2


a = [-1, -2, 3]
Solution().rerange(a)
print(a)

class Solution:
  """
    @param A: An integer array
    @return: An integer array
    """

  def singleNumberIII(self, A):
    # write your code here
    xor = 0
    size = len(A)
    for num in A:
      xor ^= num
    mask = xor & ~(xor - 1)
    st = 0
    fl = size - 1
    once = []
    while (st < fl):
      while (st < fl and (A[st] & mask == 0)):
        st += 1
      while (st < fl and (A[fl] & mask > 0)):
        fl -= 1
      A[st], A[fl] = A[fl], A[st]
    xor = 0
    for idx in range(st):
      xor ^= A[idx]
    once.append(xor)
    xor = 0
    for idx in range(st, size):
      xor ^= A[idx]
    once.append(xor)
    return once


# print(Solution().singleNumberIII([1, 2, 2, 3, 4, 4, 5, 3]))

class Solution:
  """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

  def removeElement(self, A, elem):
    # write your code here
    size = len(A)
    ptr = size - 1
    for i in range(size)[::-1]:
      if A[i] == elem:
        A[i], A[ptr] = A[ptr], A[i]
        ptr -= 1
    return ptr + 1


x = [0, 4, 4, 2, 2, 4, 0, 4]
print(Solution().removeElement(x, 4))
print(x)

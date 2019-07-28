class Solution:
  """
    @param A: An array of integers
    @return: An integer
    """

  def firstMissingPositive(self, A):
    # write your code here
    size = len(A)
    for i in range(size):
      if (A[i] < 1):
        A[i] = size + 1
    for i in range(size):
      val = abs(A[i])
      if val >= 1 and val <= size:
        A[val - 1] = -abs(A[val - 1])
    print(A)
    for i in range(size):
      if A[i] > 0:
        return i + 1
    return size + 1


# print(Solution().firstMissingPositive([3, 4, -1, 1]))

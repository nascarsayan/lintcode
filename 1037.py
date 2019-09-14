class Solution:
  """
  @param A: an array
  @return: is the number of global inversions is equal to the number of local inversions
  """

  def isIdealPermutation(self, A):
    # Write your code here
    li, gi, size = 0, 0, len(A)
    if size < 3:
      return True
    for i in range(size - 1):
      li += (0, 1)[A[i] > A[i + 1]]
    for i in range(1, size):
      j = i - 1
      tn = A[i]
      while (j >= 0 and A[j] > tn):
        A[j + 1] = A[j]
        j -= 1
      j += 1
      A[j] = tn
      gi += i - j
    print(A)
    print(li, gi)
    return li == gi


print(Solution().isIdealPermutation([1, 2, 0]))

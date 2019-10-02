class Solution:
  """
  @param: A: An integer array
  @return: A list of integers includes the index of the first number and the index of the last number
  """

  def continuousSubarraySum(self, A):
    # write your code here
    size = len(A)
    if size == 0:
      return [None, None]
    mx = [A[0], 0, 0]
    ptr = 0
    curr = [0, ptr, -1]
    while (ptr < size):
      curr[0] += A[ptr]
      curr[-1] += 1
      if mx[0] < curr[0]:
        mx = curr[:]
      if curr[0] < 0:
        curr[0] = 0
        curr[1] = ptr + 1
      ptr += 1
    return mx[1:]


print(Solution().continuousSubarraySum([-2, 0, 0, 1, -1, -1]))

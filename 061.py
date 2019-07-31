class Solution:
  """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

  def searchRange(self, A, target):
    # write your code here
    size = len(A)
    st = 0
    fl = size - 1
    hit = None
    while st <= fl:
      mid = (st + fl) >> 1
      if A[mid] == target:
        hit = mid
        break
      if A[mid] < target:
        st = mid + 1
      else:
        fl = mid - 1
    if hit is None:
      return [-1, -1]
    st = fl = hit
    while (st > 0 and A[st - 1] == target):
      st -= 1
    while (fl < size - 1 and A[fl + 1] == target):
      fl += 1
    return [st, fl]


# print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

class Solution:
  """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

  def findMinIdx(self, nums):
    # write your code here
    size = len(nums)
    if size == 0:
      return None
    if nums[0] <= nums[-1]:
      return 0
    st = 0
    fl = size - 2
    while (st <= fl):
      mid = (st + fl) // 2
      if nums[mid] > nums[mid + 1]:
        return mid + 1
      if nums[st] > nums[st + 1]:
        return st + 1
      if nums[fl] > nums[fl + 1]:
        return fl + 1
      if nums[mid] < nums[fl]:
        fl = mid
      else:
        st = mid + 1
    return None

  """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

  def search(self, A, target):
    # write your code here
    size = len(A)
    if size == 0:
      return -1
    shift = self.findMinIdx(A)
    st = 0
    fl = size - 1
    while (st <= fl):
      mid = (st + fl) // 2
      shmid = (mid + shift) % size
      if (A[shmid] == target):
        return shmid
      if (A[shmid] < target):
        st = mid + 1
      else:
        fl = mid - 1
    return -1


# print(Solution().search([4, 5, 1, 2, 3], 1))

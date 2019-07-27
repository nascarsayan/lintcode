class Solution:
  """
    @param nums: An integer array
    @return: nothing
    """

  def chainRotate(self, nums, l, st, shf):
    idx = st
    while (True):
      newIdx = (idx + shf) % l
      if (newIdx == st):
        break
      nums[st], nums[newIdx] = nums[newIdx], nums[st]
      idx = newIdx

  def gcd(self, n1, n2):
    while (n1 != 0):
      n1, n2 = n2 % n1, n1
    return n2

  def recoverRotatedSortedArray(self, nums):
    # write your code here
    l = len(nums)
    rotate = False
    for idx in range(l - 1):
      if nums[idx] > nums[idx + 1]:
        rotate = True
        break
    if not rotate:
      return
    shf = l - idx - 1
    self.chainRotate(nums, l, 0, shf)
    nsets = self.gcd(l, shf)
    if (nsets != 1):
      for st in range(1, nsets):
        self.chainRotate(nums, l, st, shf)


# nums = [3, 4, 5, 6, 1, 2]
# Solution().recoverRotatedSortedArray(nums)
# print(nums)

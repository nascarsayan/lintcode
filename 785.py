class Solution:
  """
  @param nums:
  @return: nothing
  """

  def maxWeight(self, nums):
    # write your code here
    nr = len(nums)
    if nr == 0:
      return 0
    nc = len(nums[0])
    if nc == 0:
      return 0
    for ir in range(1, nr):
      nums[ir][-1] += nums[ir - 1][-1]
    for ic in range(nc - 1)[::-1]:
      nums[0][ic] += nums[0][ic + 1]
    for ir in range(1, nr):
      for ic in range(nc - 1)[::-1]:
        nums[ir][ic] += max(nums[ir][ic + 1], nums[ir - 1][ic])
    return nums[-1][0]

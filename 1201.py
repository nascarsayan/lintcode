class Solution:
  """
  @param nums: an array
  @return: the Next Greater Number for every element
  """

  def nextGreaterElements(self, nums):
    # Write your code here
    size = len(nums)
    if size == 0:
      return nums
    maxi, mv = max(list(enumerate(nums)), key=lambda x: x[1])
    nex = [-1] * size
    stac = [mv]
    for i in range(size - 1, 0, -1):
      aci = (i + maxi) % size
      while (len(stac) > 0 and stac[-1] <= nums[aci]):
        stac.pop(-1)
      if len(stac) > 0:
        nex[aci] = stac[-1]
      stac.append(nums[aci])
    return nex

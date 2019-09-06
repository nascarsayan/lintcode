class Solution:
  """
  @param nums: an array of integers
  @return: the product of all the elements of nums except nums[i].
  """

  def productExceptSelf(self, nums):
    # write your code here
    size = len(nums)
    if size == 0:
      return nums
    lp, rp = [1], [1]
    for idx in range(size - 1):
      lp.append(lp[-1] * nums[idx])
      rp.insert(0, rp[0] * nums[size - 1 - idx])
    for idx in range(size):
      lp[idx] = lp[idx] * rp[idx]
    return lp

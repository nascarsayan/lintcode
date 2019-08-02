class Solution:
  """
    @param: nums: A list of integers
    @return: nothing
    """

  def wiggleSort(self, nums):
    # write your code here
    size = len(nums)
    for idx in range(size - 1):
      par = idx % 2
      if ((par == 0 and nums[idx] > nums[idx + 1]) or
          (par == 1 and nums[idx] < nums[idx + 1])):
        nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

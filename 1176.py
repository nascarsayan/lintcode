class Solution:
  """
  @param nums: an array
  @return: the corresponding expression in string format
  """

  def optimalDivision(self, nums):
    # Write your code here
    size = len(nums)
    if size == 0:
      return ''
    if size == 1:
      return '{}'.format(nums[0])
    if size == 2:
      return '{}/{}'.format(nums[0], nums[1])
    return '{}/({})'.format(nums[0], '/'.join(list(map(str, nums[1:]))))


print(Solution().optimalDivision([1000, 1000]))

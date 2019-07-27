class Solution:
  """
    @param: nums: a list of integers
    @return: find a  majority number
    """

  def majorityNumber(self, nums):
    # write your code here
    l = len(nums)
    if l == 0:
      return None
    if l == 1:
      return nums[0]
    majIdx = 0
    cnt = 1
    for i, num in enumerate(nums[1:]):
      if num == nums[majIdx]:
        cnt += 1
      else:
        cnt -= 1
      if cnt == 0:
        majIdx = i
        cnt = 1
    return nums[majIdx]


# print(Solution().majorityNumber([1, 1, 2, 1, 2, 2, 2]))

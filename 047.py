class Solution:
  """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """

  def majorityNumber(self, nums):
    # write your code here
    l = len(nums)
    if l == 0:
      return None
    if l == 1:
      return nums[0]
    maj1 = None
    cnt1 = 0
    maj2 = None
    cnt2 = 0
    for num in nums:
      if num == maj1:
        cnt1 += 1
      elif num == maj2:
        cnt2 += 1
      elif cnt1 == 0:
        maj1 = num
        cnt1 = 1
      elif cnt2 == 0:
        maj2 = num
        cnt2 = 1
      else:
        cnt1 -= 1
        cnt2 -= 1
    cnt1 = cnt2 = 0
    for num in nums:
      if num == maj1:
        cnt1 += 1
      elif num == maj2:
        cnt2 += 1
    if cnt1 > l // 3:
      return maj1
    return maj2


# print(Solution().majorityNumber([99, 2, 99, 2, 99, 3, 3]))

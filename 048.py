class Solution:
  """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

  def majorityNumber(self, nums, k):
    # write your code here
    l = len(nums)
    if l == 0:
      return None
    if l < k:
      return nums[0]
    nums.sort()
    ele = None
    cnt = 0
    for num in nums:
      if num != ele:
        ele = num
        cnt = 1
      else:
        cnt += 1
        if cnt > l // k:
          return num
    return None

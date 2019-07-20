class Solution:
  """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

  def partitionArray(self, nums, k):
    # write your code here
    il = 0
    ir = len(nums) - 1
    while (il <= ir):
      while (il <= ir and nums[il] < k):
        il += 1
      while (il <= ir and nums[ir] >= k):
        ir -= 1
      if (il <= ir):
        nums[il], nums[ir] = nums[ir], nums[il]
        il += 1
        ir -= 1
    return il


# print(Solution().partitionArray([3, 2, 2, 1], 2))
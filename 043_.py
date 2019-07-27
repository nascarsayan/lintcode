class Solution:
  """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """

  def maxSubArray(self, nums, k):
    # write your code here
    l = len(nums)
    ninf = float('-inf')
    if k > l:
      return ninf
    total = 0
    for _ in range(k):
      csum = 0
      maxsum = ninf
      cst = 0
      maxst = -1
      maxfl = l
      for idx in range(l):
        if csum == 0:
          cst = idx
        csum += nums[idx]
        if csum > maxsum:
          maxsum = csum
          maxst = cst
          maxfl = idx
        if csum <= 0:
          csum = 0
      print(nums)
      total += maxsum
      for idx in range(maxst, maxfl + 1):
        nums[idx] = ninf
    return total


print(Solution().maxSubArray([-1, 4, -2, 3, -2, 3], 2))

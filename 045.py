class Solution:
  """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

  def kadane(self, nums, ismin=False, rtl=False):
    l = len(nums)
    newnums = None
    if ismin:
      newnums = [-num for num in nums]
    else:
      newnums = nums[:]
    if rtl:
      newnums.reverse()
    maxVals = [None] * l
    s = 0
    maxVals[0] = newnums[0]
    if maxVals[0] > 0:
      s = maxVals[0]
    for idx in range(1, l):
      s += newnums[idx]
      maxVals[idx] = max(maxVals[idx - 1], s)
      if s < 0:
        s = 0
    if ismin:
      maxVals = [-v for v in maxVals]
    if rtl:
      maxVals.reverse()
    return maxVals

  def maxDiffSubArrays(self, nums):
    # write your code here
    Lmax = self.kadane(nums)
    Lmin = self.kadane(nums, True)
    Rmax = self.kadane(nums, False, True)
    Rmin = self.kadane(nums, True, True)
    ninf = float('-inf')
    maxdiff = ninf
    for idx, _ in enumerate(nums[1:]):
      maxdiff = max(
          abs(Lmax[idx] - Rmin[idx + 1]), abs(Rmax[idx + 1] - Lmin[idx]),
          maxdiff)
    return maxdiff


print(Solution().maxDiffSubArrays([1, 2, -3, 1]))
class Solution:

  def findDuplicates(self, nums):
    dups = []
    for idx in range(len(nums)):
      v = nums[abs(nums[idx]) - 1]
      if v < 0:
        dups.append(abs(nums[idx]))
      else:
        nums[abs(nums[idx]) - 1] *= -1
    return dups


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

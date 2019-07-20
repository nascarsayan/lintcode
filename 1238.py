class Solution:

  def findDuplicates(self, nums):
    for num in nums:
      nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
    for num in nums:
      nums[abs(num) - 1] = -nums[abs(num) - 1]
    dups = []
    for i, num in enumerate(nums):
      if (num < 0):
        dups.append(i + 1)
    return dups


# print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

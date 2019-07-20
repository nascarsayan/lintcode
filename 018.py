# https://www.lintcode.com/problem/subsets-ii/

from collections import defaultdict

class Solution:
  """
  @param nums: A set of numbers.
  @return: A list of lists. All valid subsets.
  """
  def subsetsWithDup(self, nums):
    # write your code here
    nums.sort()
    powset = [[]]
    firstInd = defaultdict(int)
    for inum in range(len(nums)):
      st = 0
      if (nums[inum] in firstInd):
        st = powset.index([nums[inum]] * (inum - firstInd[nums[inum]]))
      else:
        firstInd[nums[inum]] = inum
      for ipow in range(st, len(powset)):
        powset.append(powset[ipow] + [nums[inum]])
    return powset

print(Solution().subsetsWithDup([5, 5, 5, 5]))

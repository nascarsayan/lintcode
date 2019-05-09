# https://www.lintcode.com/problem/kth-largest-element/

from random import randint

class Solution:
  """
  @param n: An integer
  @param nums: An array
  @return: the Kth largest element
  """
  def kthLargestElement(self, n, nums):
    # write your code here
    l = len(nums)
    pivotInd = randint(0, l - 1)
    PIVPOS = l - 1
    nums[pivotInd], nums[PIVPOS] = nums[PIVPOS], nums[pivotInd]
    i = 0
    j = l - 2
    while (i <= j):
      if (nums[i] > nums[PIVPOS]):
        i += 1
      if (nums[j] <= nums[PIVPOS]):
        j -= 1
      if (i < j and nums[i] < nums[PIVPOS] and nums[j] >= nums[PIVPOS]):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[PIVPOS], nums[i] = nums[i], nums[PIVPOS]
    if (i + 1 == n):
      return nums[i]
    if (i + 1 > n):
      return self.kthLargestElement(n, nums[:i])
    return self.kthLargestElement(n - i - 1, nums[i + 1:])
    
print(Solution().kthLargestElement(3, [9,3,2,4,8]))
    
class Solution:
  """
  @param nums: the given array
  @return: the minimum difference between their sums
  """

  def findMin(self, nums):
    # write your code here
    arrsum = sum(nums)
    nr, nc = len(nums), 1 + (arrsum // 2)
    tot = {0}
    mx = float('-inf')
    for ir in range(nr):
      ntot = set()
      for et in tot:
        el = et + nums[ir]
        if el < nc and el not in tot:
          ntot.add(el)
          mx = max(mx, el)
      tot.update(ntot)
    return arrsum - 2 * mx


print(Solution().findMin([1, 5, 6, 11]))

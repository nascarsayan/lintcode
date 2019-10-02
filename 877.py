class Solution:
  """
  @param nums: a list of integer
  @return: return a boolean
  """

  def splitArray(self, nums):
    # write your code here
    size = len(nums)
    if size < 7:
      return False
    tot = nums[:]
    for i in range(1, size):
      tot[i] += tot[i - 1]
    for mid in range(3, size - 3):
      feas = set()
      for d1 in range(1, mid - 1):
        if tot[d1 - 1] == tot[mid - 1] - tot[d1]:
          feas.add(tot[d1 - 1])
      for d2 in range(mid + 2, size - 1):
        if (tot[d2 - 1] - tot[mid] == tot[-1] -
            tot[d2]) and tot[-1] - tot[d2] in feas:
          return True
    return False


print(Solution().splitArray([1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]))

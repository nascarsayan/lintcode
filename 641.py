class Solution:
  """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

  def findMissingRanges(self, nums, lower, upper):
    # write your code here
    invs = []
    nums = [lower - 1] + nums + [upper + 1]
    st, fl = 0, len(nums) - 1
    for i in range(st, fl):
      dif = nums[i + 1] - nums[i]
      if dif == 2:
        invs.append(str(nums[i] + 1))
      elif dif > 2:
        invs.append('%d->%d' % (nums[i] + 1, nums[i + 1] - 1))
    return invs


print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))

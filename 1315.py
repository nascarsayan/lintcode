class Solution:
  """
  @param nums:  a sorted integer array without duplicates
  @return: the summary of its ranges
  """

  def summaryRanges(self, nums):
    # Write your code here
    size = len(nums)
    if size == 0:
      return []
    res = []
    rans = [[nums[0], nums[0]]]
    for i in range(1, size):
      if nums[i] - nums[i - 1] != 1:
        rans.append([nums[i], nums[i]])
      else:
        rans[-1][1] = nums[i]
    for st, fl in rans:
      if st == fl:
        res.append('{}'.format(st))
      else:
        res.append('{}->{}'.format(st, fl))
    return res


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))

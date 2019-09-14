class Solution:
  """
  @param nums: the gievn integers
  @return: the total Hamming distance between all pairs of the given numbers
  """

  def totalHammingDistance(self, nums):
    # Write your code here
    size = len(nums)
    if size < 2:
      return 0
    tot = 0
    for p in range(32):
      ones = 0
      for num in nums:
        ones += (num >> p) & 1
      tot += ones * (size - ones)
    return tot


print(Solution().totalHammingDistance([4, 14, 2]))

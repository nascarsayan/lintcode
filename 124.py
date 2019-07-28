class Solution:
  """
    @param nums: A list of integers
    @return: An integer
    """

  def longestConsecutive(self, nums):
    # write your code here
    if len(nums) == 0:
      return 0
    nset = set(nums)
    maxcon = 1
    for num in nums:
      if num - 1 not in nset:
        con = 1
        while num + con in nset:
          con += 1
        maxcon = max(maxcon, con)
    return maxcon


# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

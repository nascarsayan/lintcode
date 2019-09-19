class Solution:
  """
    @param nums: An array of integers
    @return: An integer
    """

  def findMissing(self, nums):
    # write your code here
    return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)


print(Solution().findMissing([9, 8, 7, 6, 2, 0, 1, 5, 4]))

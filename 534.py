class Solution:
  """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """

  def houseRobber2(self, nums):
    # write your code here
    size = len(nums)
    if size == 0:
      return 0
    if size < 4:
      return max(nums)

    def solve(nums):
      size = len(nums)
      for idx in range(2, size):
        nums[idx] = max(nums[idx - 1], nums[idx] + nums[idx - 2])
      return nums[idx]

    return max(solve(nums[:-1]), solve(nums[1:]))


print(Solution().houseRobber2([1, 3, 2, 1, 5]))

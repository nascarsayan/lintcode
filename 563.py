class Solution:
  """
  @param nums: an integer array and all positive numbers
  @param target: An integer
  @return: An integer
  """

  def backPackV(self, nums, target):
    # write your code here
    nr, nc = len(nums), target + 1
    dp = [1] + [0] * target
    for ir in range(nr):
      for ic in range(nums[ir], nc)[::-1]:
        dp[ic] += dp[ic - nums[ir]]
    return dp[-1]

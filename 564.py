class Solution:
  """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

  def backPackVI(self, nums, target):
    # write your code here
    nums.sort()
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
      for num in nums:
        if num > i:
          break
        dp[i] += dp[i - num]
    return dp[target]


print(Solution().backPackVI([1, 2, 4], 4))

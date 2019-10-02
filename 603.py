class Solution:
  """
  @param: nums: a set of distinct positive integers
  @return: the largest subset
  """

  def largestDivisibleSubset(self, nums):
    # write your code here
    nums.sort()
    size = len(nums)
    res = []
    if size < 2:
      return res
    dp = [(0, -1, i) for i in range(size)]
    for i in range(1, size):
      for j in range(i):
        if nums[i] % nums[j] == 0:
          dp[i] = max(dp[i], (dp[j][0] + 1, j, i))
    mx = max(dp)
    if mx[0] == 0:
      return [nums[0]]
    while (mx[1] >= 0):
      res.append(nums[mx[2]])
      mx = dp[mx[1]]
    res.append(nums[mx[2]])
    return list(reversed(res))


print(Solution().largestDivisibleSubset([1, 2, 4, 8]))

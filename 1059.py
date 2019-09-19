from collections import Counter, defaultdict


class Solution:
  """
    @param nums: a list of integers
    @return: return a integer
    """

  def deleteAndEarn(self, nums):
    # write your code here
    if len(nums) == 0:
      return 0
    dp = defaultdict(int)
    cnt = Counter(nums)
    mx = max(cnt.keys())
    for num in range(1, mx + 1):
      dp[num] = max(dp[num - 1], dp[num - 2] + cnt[num] * num)
    return max(dp.values())


print(Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]))

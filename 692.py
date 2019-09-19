from collections import Counter


class Solution:
  """
  @param nums: the given array
  @param k: the window size
  @return: the sum of the count of unique elements in each window
  """

  def slidingWindowUniqueElementsSum(self, nums, k):
    # write your code here
    size = len(nums)
    k = min(k, size)
    if k == 0:
      return []
    cnt = Counter()
    for i in range(k):
      cnt[nums[i]] += 1
    uniq = len([1 for k in cnt if cnt[k] == 1])
    res = uniq
    for i in range(k, size):
      if nums[i] != nums[i - k]:
        cnt[nums[i]] += 1
        cnt[nums[i - k]] -= 1
        if cnt[nums[i]] == 1:
          uniq += 1
        if cnt[nums[i - k]] == 1:
          uniq += 1
        if cnt[nums[i]] == 2:
          uniq -= 1
        if cnt[nums[i - k]] == 0:
          uniq -= 1
      res += uniq
    return res


print(Solution().slidingWindowUniqueElementsSum([1, 1, 1, 1, 1, 1], 2))

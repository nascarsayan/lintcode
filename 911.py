class Solution:
  """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """

  def maxSubArrayLen(self, nums, k):
    # Write your code here
    size = len(nums)
    mx = 0
    if size == 0:
      return mx
    app1 = {}
    total = 0
    for i, num in enumerate(nums):
      total += num
      if total == k:
        mx = max(mx, i + 1)
      else:
        if total - k in app1:
          mx = max(mx, i - app1[total - k])
        if total not in app1:
          app1[total] = i
    return mx


print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))

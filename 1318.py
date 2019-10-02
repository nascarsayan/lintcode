class Solution:
  """
  @param nums: the given array
  @param k: the given k
  @param t: the given t
  @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j]
  is at most t and the absolute difference between i and j is at most k.
  """

  def containsNearbyAlmostDuplicate(self, nums, k, t):
    # Write your code here
    size = len(nums)
    bucket, wt = {}, t + 1
    for i in range(size):
      bi = nums[i] // wt
      for bj in range(bi - 1, bi + 2):
        if bj in bucket and abs(bucket[bj] - nums[i]) <= t:
          return True
      bucket[bi] = nums[i]
      if i >= k:
        del bucket[nums[i - k] // wt]
    return False

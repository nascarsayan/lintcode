from collections import defaultdict


class Solution:
  """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

  def majorityNumber(self, nums, k):
    # write your code here
    cnt = defaultdict(int)
    size = len(nums)
    for num in nums:
      cnt[num] += 1
      if cnt[num] > size // k:
        return num
    return None

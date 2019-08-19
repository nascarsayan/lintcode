from collections import Counter


class Solution:
  """
  @param nums: the given array
  @param k: the given k
  @return: the k most frequent elements
  """

  def topKFrequent(self, nums, k):
    # Write your code here
    cnt = Counter(nums)
    return list(map(lambda x: x[0], cnt.most_common(k)))

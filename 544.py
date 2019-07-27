import heapq


class Solution:
  """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

  def topk(self, nums, k):
    # write your code here
    nums = [-x for x in nums]
    size = len(nums)
    heapq.heapify(nums)
    maxk = []
    for ik in range(min(k, size)):
      maxk.append(-heapq.heappop(nums))
    return maxk


# print(Solution().topk([3, 10, 1000, -99, 4, 100], 3))

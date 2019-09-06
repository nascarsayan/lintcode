import heapq


class Solution:
  """
  @param nums1: List[int]
  @param nums2: List[int]
  @param k: an integer
  @return: return List[List[int]]
  """

  def kSmallestPairs(self, nums1, nums2, k):
    # write your code here
    inf = float('inf')
    hp = [(inf, [0, inf])]
    n1s = len(nums1)
    n2s = len(nums2)
    if k > n1s * n2s:
      k = n1s * n2s
    res = []
    idx = 0
    size = 0
    while (size < k):
      if idx < n1s and hp[0][0] > nums1[idx] + nums2[0]:
        for num in nums2:
          heapq.heappush(hp, (nums1[idx] + num, [nums1[idx], num]))
        idx += 1
      v, e = heapq.heappop(hp)
      res.append(e)
      size += 1
    return res

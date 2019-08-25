from collections import Counter


class Solution:
  """
  @param nums1: an integer array
  @param nums2: an integer array
  @return: an integer array
  """

  def intersection(self, nums1, nums2):
    # write your code here
    cnt1 = Counter(nums1)
    cnt2 = Counter(nums2)
    insc = []
    for k in set(cnt1.keys()).intersection(cnt2.keys()):
      insc.extend([k] * min(cnt1[k], cnt2[k]))
    return insc
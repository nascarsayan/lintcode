from collections import defaultdict


class Solution:
  """
  @param nums: a list of integers
  @return: return a boolean
  """

  def isPossible(self, nums):
    # write your code here
    cnt, tail = defaultdict(int), defaultdict(int)
    for num in nums:
      cnt[num] += 1
    for num in nums:
      if cnt[num] < 1:
        continue
      if tail[num - 1] > 0:
        tail[num - 1] -= 1
        tail[num] += 1
      elif all(cnt[num + dn] > 0 for dn in [1, 2]):
        cnt[num + 1] -= 1
        cnt[num + 2] -= 1
        tail[num + 2] += 1
      else:
        return False
      cnt[num] -= 1
    return True

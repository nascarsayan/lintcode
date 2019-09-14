import math


class Solution:
  """
  @param ages: 
  @return: nothing
  """

  def numFriendRequests(self, ages):
    #
    size = max(ages) + 1
    cnt = [0] * size
    for age in ages:
      cnt[age] += 1
    pre = cnt[:]
    tot = 0
    for i in range(1, size):
      pre[i] += pre[i - 1]
    for i in range(15, size):
      j = math.ceil(7 + (i + 1) / 2)
      ppl = pre[i] - pre[j - 1]
      if ppl > 0:
        tot += (ppl - 1) * cnt[i]
    return tot


print(Solution().numFriendRequests([16, 16]))

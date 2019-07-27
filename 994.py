from collections import defaultdict


class Solution:
  """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """

  def findMaxLength(self, nums):
    # Write your code here
    opps = map(lambda x: 2 * x - 1, nums)
    sumopps = []
    csum = 0
    first = {}
    last = {}
    candi = [0, 0]
    for i, opp in enumerate(opps):
      csum += opp
      sumopps.append(csum)
      if csum == 0:
        candi[0] = i + 1
    for i, s in enumerate(sumopps):
      if s not in first:
        first[s] = i
      else:
        last[s] = i
    lastkeys = last.keys()
    if len(lastkeys) > 0:
      mlen = 0
      for k in lastkeys:
        if last[k] - first[k] > mlen:
          mlen = last[k] - first[k]
      candi[1] = mlen

    return max(candi)


# print(Solution().findMaxLength([0, 1, 0]))

from collections import defaultdict


class Solution:
  """
  @param answers: some subset of rabbits (possibly all of them) tell
  @return: the minimum number of rabbits that could be in the forest.
  """

  def numRabbits(self, answers):
    # write your code here
    cnt = defaultdict(int)
    for ans in answers:
      cnt[ans] += 1
    v = cnt.pop(0, 0)
    for noth in cnt.keys():
      dec = noth * (noth + 1)
      v += (noth + 1) * ((cnt[noth] + dec - 1) // dec)
    return v


print(Solution().numRabbits([10, 10, 10]))

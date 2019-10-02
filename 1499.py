from collections import Counter


class Solution:
  """
  @param N:
  @return: return true or false
  """

  def reorderedPowerOf2(self, N):
    # write your code here
    p2 = 1
    p2s = set()
    for i in range(33):
      cnt = Counter(str(p2))
      p2s.add(tuple(sorted(cnt.most_common())))
      p2 <<= 1
    return tuple(sorted(Counter(str(N)).most_common())) in p2s


print(Solution().reorderedPowerOf2(46))

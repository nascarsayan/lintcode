from collections import defaultdict, Counter


class Solution:
  """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """

  def groupAnagrams(self, strs):
    # write your code here
    size = len(strs)
    ana = defaultdict(list)
    for i in range(size):
      cnt = Counter(strs[i])
      nk = []
      for k in sorted(cnt.keys()):
        nk.extend([k, str(cnt[k])])
      ana[','.join(nk)].append(strs[i])
    return list(ana.values())

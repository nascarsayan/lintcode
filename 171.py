from collections import Counter, defaultdict
import json


class Solution:
  """
    @param strs: A list of strings
    @return: A list of strings
    """

  def anagrams(self, strs):
    # write your code here
    cnts = defaultdict(list)
    anas = []
    for i, st in enumerate(strs):
      k = json.dumps(Counter(st), sort_keys=True)
      cnts[k].append(i)
      sizek = len(cnts[k])
      if sizek == 2:
        anas.append(strs[cnts[k][0]])
      if sizek > 1:
        anas.append(strs[cnts[k][-1]])
    return anas


# print(Solution().anagrams(['ab', 'ba', 'cd', 'dc']))

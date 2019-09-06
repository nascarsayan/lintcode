from collections import defaultdict


class Solution:
  """
  @param S: a string
  @return: a list of integers representing the size of these parts
  """

  def partitionLabels(self, S):
    # Write your code here
    occ = defaultdict(list)
    ssize = len(S)
    for i, c in enumerate(S):
      occ[c].append(i)
      if len(occ[c]) == 3:
        occ[c].pop(1)
    invls = []
    for k in occ.keys():
      if len(occ[k]) == 2:
        invls.append(occ[k])
    invls.sort(key=lambda x: x[0])
    i = 0
    while (i < len(invls) - 1):
      if invls[i + 1][0] < min(invls[i][1], invls[i + 1][1]):
        invls[i] = [invls[i][0], max(invls[i][1], invls[i + 1][1])]
        invls.pop(i + 1)
      else:
        i += 1
    invsz = len(invls)
    if invsz == 0:
      return [1] * ssize
    parts = []
    parts.extend([1] * (invls[0][0]))
    for i in range(invsz - 1):
      parts.append(invls[i][1] - invls[i][0] + 1)
      parts.extend([1] * (invls[i + 1][0] - invls[i][1] - 1))
    parts.append(invls[-1][1] - invls[-1][0] + 1)
    parts.extend([1] * (ssize - 1 - invls[-1][1]))
    return parts


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))